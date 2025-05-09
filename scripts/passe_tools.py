from pathlib import Path

# === Répertoires partagés entre passes ===

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Passe 0
INPUT_DIR_0 = DATA_DIR / "00docx_tab"
OUTPUT_DIR_0 = DATA_DIR / "01docx_lin_in"
IMAGE_DIR_0 = OUTPUT_DIR_0 / "images"
LOG_DIR_0 = OUTPUT_DIR_0 / "log"

# Passe 1
INPUT_DIR_1 = DATA_DIR / "01docx_lin_in"
OUTPUT_DIR_1 = DATA_DIR / "02text_p1_out"
IMAGE_DIR_1 = OUTPUT_DIR_1 / "images"
LOG_DIR_1 = OUTPUT_DIR_1 / "log"

# Passe 2
INPUT_DIR_2 = DATA_DIR / "02text_p1_out"
OUTPUT_DIR_2 = DATA_DIR / "03text_p2_checked"
LOG_DIR_2 = OUTPUT_DIR_2 / "log"

# === Structure standard de l'en-tête ===

ENTETE_STRUCTURE = [
    "##Identification",
    "#Script",
    "#Run at",
    "#ID file",
    "##LANG-",
    "#ID",
    "#Version",
    "#Date",
    "#Author",
    "##Introduction",
    "##Work Start"
]

def verifier_entete_lignes(lignes):
    """Retourne True si les balises d'en-tête standard sont toutes partiellement présentes dans les lignes."""
    return all(any(att in ligne for ligne in lignes) for att in ENTETE_STRUCTURE)

from datetime import datetime

def generer_entete(langue, id_code, nom_fichier, version_script="unknown", version="", date="", auteur=""):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    return [
        "##Identification",
        f"#Script : {version_script}.py",
        f"#Run at : {now}",
        f"#ID file : {nom_fichier}",
        f"##LANG-{langue}",
        f"#ID : {id_code}",
        f"#Version : {version}",
        f"#Date : {date}",
        f"#Author : {auteur}",
        "",
        "##Introduction",
        "",
        "##Work Start"
    ]
