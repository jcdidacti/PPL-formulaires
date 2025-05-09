# ==============================================================================
# Script : passe1_simplifiee.py
# Objectif : Extraire texte et images d'un .docx issu de la passe0
# Date : 2025-05-08
# Version : v1.00
# ==============================================================================

import os
from pathlib import Path
from docx import Document
from passe_tools import extraire_images, lire_entete
from docx.oxml.ns import qn
from hashlib import sha1
from datetime import datetime

# Répertoires
base_dir = Path(__file__).parent
SOURCE_DIR = base_dir / "fichiers_passe0"
TXT_OUT_DIR = base_dir / "fichiers_passe1_txt"
IMG_OUT_DIR = base_dir / "fichiers_passe1_images"

for d in [TXT_OUT_DIR, IMG_OUT_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def traiter_docx(docx_path):
    doc = Document(docx_path)
    base_name = docx_path.stem
    image_dir = IMG_OUT_DIR / base_name
    image_dir.mkdir(exist_ok=True)

    images = extraire_images(doc, image_dir, base_name)

    # Texte brut
    texte = []
    for para in doc.paragraphs:
        line = para.text.strip()
        if line:
            texte.append(line)

    # Sauvegarde TXT
    txt_file = TXT_OUT_DIR / f"{base_name}.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("\n".join(texte))
    print(f"✅ {base_name} traité : {len(images)} image(s), {len(texte)} lignes de texte.")

# Traitement de tous les fichiers .docx
for fichier in SOURCE_DIR.glob("*.docx"):
    print(f"🔍 Traitement : {fichier.name}")
    traiter_docx(fichier)