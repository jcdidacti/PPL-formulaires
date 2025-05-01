# ============================================================================
# Script : passe2_validator.py (v1.07-dev)
# Objectif : Valider la structure du document par langue (FR/DE), afficher les erreurs sous chaque ligne (console et annotated)
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
    lines = path_txt.read_text(encoding="utf-8").splitlines()
    annotations = []
    erreurs = []
    erreurs_par_ligne = {}
    phase = ""
    bloc_langue_en_cours = False
    en_attente_de_A = False
    work_stop_present = False
    end_form_present = False
    def enregistrer_erreur(lno, msg):
        print(f"!! ERREUR [Ligne {lno:03}]: {msg}")
        erreurs.append((lno, msg))
        erreurs_par_ligne.setdefault(lno, []).append(f"     ^-- {msg}")
    for i, ligne in enumerate(lines):
        num = i + 1
        ligne_strip = ligne.strip()
        ligne_annot = f"{num:04} | {ligne}"
        if balise_id.match(ligne_strip):
            phase = "ID"; bloc_langue_en_cours = False
            expected = ["## Identification", "#Script", "#Run at", "#ID file", "##LANG"]
            for j, label in enumerate(expected):
                if i + j >= len(lines) or not lines[i + j].strip().startswith(label):
                    enregistrer_erreur(i + j + 1, f"Ligne attendue : {label}")
        elif balise_lang.match(ligne_strip):
            if bloc_langue_en_cours and not work_stop_present:
                enregistrer_erreur(num, "##LANG trouvé alors que le bloc précédent n'est pas terminé par ## Work Stop")
            if phase != "ID":
                enregistrer_erreur(num, "Balise ##LANG trouvée sans ## Identification avant")
                for back in range(1, 6):
                    j = i - back
                    if j >= 0 and "Identification" in lines[j] and not lines[j].strip().startswith("##"):
                        enregistrer_erreur(j + 1, "Balise ## Identification absente avant ce bloc de langue")
                        break
            phase = "LANG"; bloc_langue_en_cours = True
            en_attente_de_A = False
            work_stop_present = False
        elif balise_q.match(ligne_strip):
            if not bloc_langue_en_cours:
                enregistrer_erreur(num, "#Q rencontré hors bloc de langue")
            if en_attente_de_A:
                enregistrer_erreur(num, "#Q rencontré alors qu'une question précédente n'a pas de #A")
            en_attente_de_A = True
        elif balise_a.match(ligne_strip):
            if not en_attente_de_A:
                enregistrer_erreur(num, "#A rencontré sans question #Q préalable")
            en_attente_de_A = False
        elif balise_stop.match(ligne_strip):
            if not bloc_langue_en_cours:
                enregistrer_erreur(num, "## Work Stop rencontré hors bloc de langue")
            work_stop_present = True
            if en_attente_de_A:
                enregistrer_erreur(num, "## Work Stop trouvé alors qu'une question n'a pas de réponse")
            bloc_langue_en_cours = False
            phase = "STOP"
        elif balise_end.match(ligne_strip):
            end_form_present = True
            phase = "END"
        print(f"-- ligne {num:03}: {ligne_strip}")
        annotations.append(ligne_annot)
        if num in erreurs_par_ligne:
            annotations.extend(erreurs_par_ligne[num])
    if not end_form_present:
        enregistrer_erreur(len(lines), "Balise ## End of Form absente")
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
