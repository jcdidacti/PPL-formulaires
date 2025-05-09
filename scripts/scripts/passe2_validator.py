# ============================================================================
# Script : passe2_validator.py (v1.09d)
# Objectif : Détection des balises de structure dupliquées et questions après ##Work End
# Date : 2025-05-01
# ============================================================================

import re
from pathlib import Path
from datetime import datetime

input_dir = Path("data/02text_p1_out")
output_dir = Path("data/03txt_validated")
output_dir.mkdir(parents=True, exist_ok=True)

balises_entete = ["##Identification", "#Script", "#Run at", "#ID file", "##LANG"]
balises_description = ["#ID", "#Version", "#Date", "#Author"]
balises_structure_langue = ["##Introduction", "##Work Start", "##Work End"]
balise_form_end = "##Form End"

global_log = []

def enregistrer_erreur(erreurs, erreurs_par_ligne, lno, msg):
    print(f"!! ERREUR [Ligne {lno:03}]: {msg}")
    erreurs.append((lno, msg))
    erreurs_par_ligne.setdefault(lno, []).append(f"     ^-- {msg}")

def analyser_fichier(path_txt: Path):
    lines = path_txt.read_text(encoding="utf-8").splitlines()
    annotations = []
    erreurs = []
    erreurs_par_ligne = {}
    positions_ident = [i for i, l in enumerate(lines) if "Identification" in l]
    form_end_found = any(l.strip() == balise_form_end for l in lines)

    for i in range(len(lines)):
        annotations.append(f"{i+1:04} | {lines[i]}")

    for start in positions_ident:
        if not lines[start].strip().startswith("##Identification"):
            enregistrer_erreur(erreurs, erreurs_par_ligne, start+1, "balise mal formée : ##Identification attendue")

        for j, label in enumerate(balises_entete):
            idx = start + j
            if idx >= len(lines):
                enregistrer_erreur(erreurs, erreurs_par_ligne, idx+1, f"balise manquante : {label}")
            elif not lines[idx].strip().startswith(label):
                enregistrer_erreur(erreurs, erreurs_par_ligne, idx+1, f"balise invalide ou absente : {label}")

        for j, label in enumerate(balises_description):
            idx = start + len(balises_entete) + j
            if idx >= len(lines):
                enregistrer_erreur(erreurs, erreurs_par_ligne, idx+1, f"balise manquante : {label}")
            elif not lines[idx].strip().startswith(label):
                enregistrer_erreur(erreurs, erreurs_par_ligne, idx+1, f"balise invalide ou absente : {label}")

        fin_bloc = positions_ident[positions_ident.index(start)+1] if positions_ident.index(start)+1 < len(positions_ident) else len(lines)
        bloc_texte = lines[start:fin_bloc]

        # Vérifier la présence et l'unicité des balises de structure
        for balise in balises_structure_langue:
            occurences = [i for i, l in enumerate(bloc_texte) if l.strip() == balise]
            if len(occurences) == 0:
                enregistrer_erreur(erreurs, erreurs_par_ligne, start+1, f"balise manquante dans bloc langue : {balise}")
            elif len(occurences) > 1:
                for pos in occurences[1:]:
                    enregistrer_erreur(erreurs, erreurs_par_ligne, start + pos + 1, f"balise dupliquée : {balise}")

        # Vérifier les #Q après ##Work End
        work_end_found = False
        for i in range(start, fin_bloc):
            lstrip = lines[i].strip()
            if lstrip == "##Work End":
                work_end_found = True
            elif work_end_found and lstrip.startswith("#Q"):
                enregistrer_erreur(erreurs, erreurs_par_ligne, i+1, "#Q après ##Work End — bloc mal structuré")

    if not form_end_found:
        enregistrer_erreur(erreurs, erreurs_par_ligne, len(lines), f"balise manquante : {balise_form_end}")

    nom_base = path_txt.stem
    output_path = output_dir / f"{nom_base}.annotated.txt"
    with open(output_path, "w", encoding="utf-8") as out:
        for i, ligne in enumerate(lines):
            num = i + 1
            out.write(f"{num:04} | {ligne}\n")
            if num in erreurs_par_ligne:
                for err in erreurs_par_ligne[num]:
                    out.write(f"{err}\n")
        if 0 in erreurs_par_ligne:
            for err in erreurs_par_ligne[0]:
                out.write(f"{err}\n")

    log_path = output_dir / f"{nom_base}.log"
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("# Log de validation — passe2 (v1.09d — contrôle affiné)\n")
        log.write(f"# Fichier : {nom_base}\n\n")
        if erreurs:
            for num, msg in erreurs:
                ligne = f"[Ligne {num:03}] " if num > 0 else ""
                log.write(f"{ligne}{msg}\n")
            log.write(f"\nStatut final : ERREURS TROUVÉES ({len(erreurs)})\n")
            global_log.append(f"{nom_base} : ERREURS ({len(erreurs)})")
        else:
            log.write("Aucune erreur trouvée.\nStatut final : OK\n")
            global_log.append(f"{nom_base} : OK")

    print(f"✔ Analyse terminée : {nom_base} — {len(erreurs)} erreur(s)")

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
