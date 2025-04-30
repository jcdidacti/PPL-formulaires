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
        ligne_annot = f"{num:04} | {ligne}"

        if balise_id.match(ligne_strip):
            phase = "ID"
            bloc_langue_en_cours = False
            id_block = lines[i+1:i+5]
            for j, expected in enumerate(ident_keys):
                if j >= len(id_block) or not id_block[j].strip().startswith(expected):
                    erreurs.append((i + j + 2, f"Ligne attendue : {expected}"))

        elif balise_lang.match(ligne_strip):
            if bloc_langue_en_cours and not work_stop_present:
                erreurs.append((num, "##LANG trouvé alors que le bloc précédent n'est pas terminé par ## Work Stop"))
            if phase != "ID":
                erreurs.append((num, "Balise ##LANG trouvée sans ## Identification avant"))
            phase = "LANG"
            bloc_langue_en_cours = True
            en_attente_de_A = False
            work_stop_present = False

        elif balise_q.match(ligne_strip):
            if not bloc_langue_en_cours:
                erreurs.append((num, "#Q rencontré hors bloc de langue"))
            if en_attente_de_A:
                erreurs.append((num, "#Q rencontré alors qu'une question précédente n'a pas de #A"))
            en_attente_de_A = True

        elif balise_a.match(ligne_strip):
            if not en_attente_de_A:
                erreurs.append((num, "#A rencontré sans question #Q préalable"))
            en_attente_de_A = False

        elif balise_stop.match(ligne_strip):
            if not bloc_langue_en_cours:
                erreurs.append((num, "## Work Stop rencontré hors bloc de langue"))
            work_stop_present = True
            if en_attente_de_A:
                erreurs.append((num, "## Work Stop trouvé alors qu'une question n'a pas de réponse"))
            bloc_langue_en_cours = False
            phase = "STOP"

        elif balise_end.match(ligne_strip):
            end_form_present = True
            phase = "END"

        annotations.append(ligne_annot)

    if not end_form_present:
        erreurs.append((len(lines), "Balise ## End of Form absente"))

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