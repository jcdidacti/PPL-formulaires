# ============================================================================
# Script : passe2_validator.py (vérifie uniquement la succession Q/A)
# Objectif : Détecter les blocs Q sans A, ou A sans Q, ou fin manquante
# Date : 2025-04-30
# ============================================================================

import re
from pathlib import Path
from datetime import datetime

input_dir = Path("data/02text_p1_out")
output_dir = Path("data/03txt_validated")
output_dir.mkdir(parents=True, exist_ok=True)

balise_q = re.compile(r"^#Q#+")
balise_a = re.compile(r"^#A-+")
balise_stop = re.compile(r"^## Work Stop$", re.IGNORECASE)

global_log = []

def analyser_fichier(path_txt: Path):
    lines = path_txt.read_text(encoding="utf-8").splitlines()
    annotations = []
    erreurs = []

    en_attente_de_A = False
    work_stop_present = False

    for i, ligne in enumerate(lines):
        num = i + 1
        ligne_strip = ligne.strip()
        ligne_annot = f"{num:04} | {ligne}"

        if balise_q.match(ligne_strip):
            if en_attente_de_A:
                erreurs.append((num, "#Q rencontré alors qu'une question précédente n'a pas de #A"))
            en_attente_de_A = True

        elif balise_a.match(ligne_strip):
            if not en_attente_de_A:
                erreurs.append((num, "#A rencontré sans question #Q préalable"))
            en_attente_de_A = False

        elif balise_stop.match(ligne_strip):
            work_stop_present = True
            if en_attente_de_A:
                erreurs.append((num, "Fin du document atteinte sans réponse pour une question"))
            en_attente_de_A = False

        annotations.append(ligne_annot)

    if not work_stop_present:
        erreurs.append((len(lines), "Balise ## Work Stop absente"))

    (output_dir / f"{path_txt.stem}.annotated.txt").write_text(
        "\n".join(annotations),
        encoding="utf-8"
    )

    log_path = output_dir / f"{path_txt.stem}.log"
    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"# Log de validation — passe2 (Q/A uniquement)\n")
        log.write(f"# Fichier : {path_txt.stem}\n\n")
        if erreurs:
            for num, msg in erreurs:
                log.write(f"[Ligne {num:03}] {msg}\n")
            log.write(f"\nStatut final : ERREURS TROUVÉES ({len(erreurs)})\n")
            global_log.append(f"{path_txt.stem} : ERREURS ({len(erreurs)})")
        else:
            log.write("Aucune erreur trouvée.\nStatut final : OK\n")
            global_log.append(f"{path_txt.stem} : OK")

    print(f"✔ Analyse Q/A terminée : {path_txt.stem} — {len(erreurs)} erreur(s)")


if __name__ == "__main__":
    fichiers = list(input_dir.glob("*.txt"))
    for f in fichiers:
        analyser_fichier(f)

    global_log_path = output_dir / "_global_validation.log"
    with open(global_log_path, "w", encoding="utf-8") as g:
        g.write(f"# Log global de validation — passe2\n")
        g.write(f"# Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        g.write("# ========================================\n")
        for entry in global_log:
            g.write(entry + "\n")