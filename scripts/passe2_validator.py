# ============================================================================
# Script : passe2_validator.py (v1.04-dev)
# Objectif : Valider la structure par langue avec détection réelle des lignes ID/Version/Date/Auteur
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
balise_end = re.compile(r"^## End of Form$", re.IGNORECASE)
balise_id = re.compile(r"^## Identification$")
balise_lang = re.compile(r"^##LANG-[a-z]{2}$", re.IGNORECASE)

global_log = []

def analyser_fichier(path_txt: Path):
    ident_keys = ["##ID", "##Version", "##Date", "##Auteur"]
    lines = path_txt.read_text(encoding="utf-8").splitlines()
    annotations = []
    erreurs = []

    phase = ""
    bloc_langue_en_cours = False
    en_attente_de_A = False
    work_stop_present = False
    end_form_present = False

    for i, ligne in enumerate(lines):
        num = i + 1
        ligne_strip = ligne.strip()
        print(f"-- ligne {num:03}: {ligne_strip}")
        print(f"-- ligne {num:03}: {ligne_strip}")
        ligne_annot = f"{num:04} | {ligne}"

        if balise_id.match(ligne_strip):
            # Vérifier les 4 lignes suivantes obligatoires avant les infos de langue
            expected_headers = [("#Script", "#Script"), ("#Run at", "#Run at"), ("#ID file", "#ID file"), ("##LANG-", "##LANG")]
            for offset, (expected_prefix, label) in enumerate(expected_headers):
                if i + offset + 1 >= len(lines) or not lines[i + offset + 1].strip().startswith(expected_prefix):
                    message = f"Ligne attendue : {label}"
                message = f"Ligne attendue : {label}"
                print(f"!! ERREUR [Ligne {i + offset + 2:03}]: {message}")
                erreurs.append((i + offset + 2, message))
            phase = "ID"
            bloc_langue_en_cours = False
            print(f">> Début bloc Identification détecté à la ligne {num}")
            # Chercher dynamiquement les 4 lignes suivantes avec les balises attendues
            found = {key: False for key in ident_keys}
            for j in range(1, 10):  # limite de sécurité
                if i + j >= len(lines):
                    break
                ligne_suivante = lines[i + j].strip()
                ligne_num = i + j + 1
                for key in ident_keys:
                    if ligne_suivante.startswith(key):
                        found[key] = True
            for key in ident_keys:
                if not found[key]:
                    message = f"Ligne attendue (dans les suivantes) : {key}"

        elif balise_lang.match(ligne_strip):
            if bloc_langue_en_cours and not work_stop_present:
                message = "##LANG trouvé alors que le bloc précédent n'est pas terminé par ## Work Stop"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            if phase != "ID":
                message = "Balise ##LANG trouvée sans ## Identification avant"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            phase = "LANG"
            bloc_langue_en_cours = True
            en_attente_de_A = False
            work_stop_present = False

        elif balise_q.match(ligne_strip):
            if not bloc_langue_en_cours:
                message = "#Q rencontré hors bloc de langue"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            if en_attente_de_A:
                message = "#Q rencontré alors qu'une question précédente n'a pas de #A"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            en_attente_de_A = True

        elif balise_a.match(ligne_strip):
            if not en_attente_de_A:
                message = "#A rencontré sans question #Q préalable"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            en_attente_de_A = False

        elif balise_stop.match(ligne_strip):
            if not bloc_langue_en_cours:
                message = "## Work Stop rencontré hors bloc de langue"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            work_stop_present = True
            if en_attente_de_A:
                message = "## Work Stop trouvé alors qu'une question n'a pas de réponse"
                print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
                erreurs.append((num, message))
            bloc_langue_en_cours = False
            phase = "STOP"

        elif balise_end.match(ligne_strip):
            end_form_present = True
            phase = "END"

        annotations.append(ligne_annot)

    if not end_form_present:
        message = "Balise ## End of Form absente"
        print(f"!! ERREUR [Ligne {len(lines):03}]: {message}")
        erreurs.append((len(lines), message))

    nom_base = path_txt.stem
    output_path = output_dir / f"{nom_base}.annotated.txt"
    output_path.write_text("\n".join(annotations), encoding="utf-8")

    log_path = output_dir / f"{nom_base}.log"
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("# Log de validation — passe2 (structure générale)\n")
        log.write(f"# Fichier : {nom_base}\n\n")
        if erreurs:
            for num, msg in erreurs:
                log.write(f"[Ligne {num:03}] {msg}\n")
            log.write(f"\nStatut final : ERREURS TROUVÉES ({len(erreurs)})\n")
            global_log.append(f"{nom_base} : ERREURS ({len(erreurs)})")
        else:
            log.write("Aucune erreur trouvée.\nStatut final : OK\n")
            global_log.append(f"{nom_base} : OK")

    print(f"✔ Analyse structure terminée : {nom_base} — {len(erreurs)} erreur(s)")

if __name__ == "__main__":
    fichiers = list(input_dir.glob("*.txt"))
    for f in fichiers:
        analyser_fichier(f)

    global_log_path = output_dir / "_global_validation.log"
    with open(global_log_path, "w", encoding="utf-8") as g:
        g.write("# Log global de validation — passe2\n")
        g.write(f"# Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        g.write("# ========================================\n")
        for entry in global_log:
            g.write(entry + "\n")