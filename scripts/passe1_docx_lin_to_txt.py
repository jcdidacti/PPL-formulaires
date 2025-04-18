# ==============================================================================
# @SCRIPT_NAME_INSERT
# Script : passe2a_docx_to_txt_v2_62.py
# Objectif : Ajout de \n dans les logs individuels et globaux
# Date : 2025-04-13
# ==============================================================================

import os
import re
from pathlib import Path
from docx import Document
import zipfile
from datetime import datetime

SCRIPT_NAME = Path(__file__).name
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Répertoire racine du projet
base_dir = Path(os.path.abspath(__file__)).resolve().parent.parent
data_dir = base_dir / "data"

# Chemins de la passe 1
input_dir = data_dir / "02docx_lin_out"
output_dir = data_dir / "02text_p1_out"
image_dir = output_dir / "images"
log_dir = output_dir / "log"

# Création des dossiers de sortie si nécessaire
output_dir.mkdir(parents=True, exist_ok=True)
image_dir.mkdir(parents=True, exist_ok=True)
log_dir.mkdir(parents=True, exist_ok=True)

files = list(input_dir.glob("*.docx"))

def get_struct(language, nom_fichier, code, auteur, file_date):
    is_fr = language == "fr"
    lang_map = {
        "intro": "## Introduction",
        "intro_note": "# To be completed",
        "work_start": "## Work Start",
        "work_stop": "## Work Stop",
        "personal_data": "## Personal data",
        "personal_fields": [
            "Temps passé sur ce questionnaire :" if is_fr else "Zeitaufwand für diese Herausforderung :",
            "Code de l'élève :" if is_fr else "Schüler*in-Code :",
            "Code de vérification :" if is_fr else "Prüfcode :",
        ],
        "end": "## End of Form"
    }

    header = [
        "## Identification",
        f"#Script : {SCRIPT_NAME}",
        f"#Run at : {TIMESTAMP}",
        f"#ID file : {nom_fichier}",
        f"ID        {code}",
        f"Version   00.00",
        f"{'Date ' if is_fr else 'Datum'}     20-01-2025",
        f"{'Auteur ' if is_fr else 'Autor  '}   {auteur}",
        "",
        lang_map["intro"],
        lang_map["intro_note"],
        "",
        lang_map["work_start"]
    ]

    footer = [
        "",
        lang_map["work_stop"],
        "",
        lang_map["personal_data"]
    ] + lang_map["personal_fields"] + [lang_map["end"]]

    return header, footer

def process_blocs(bloc_liste):
    lignes_struct = []
    skip_z = False
    for ligne in bloc_liste:
        if skip_z:
            skip_z = False
            continue
        if re.match(r"^Zeitaufwand für diese Herausforderung", ligne) or re.match(r"^Temps passé sur ce questionnaire", ligne):
            skip_z = True
            continue
        if "|" in ligne:
            q, a = ligne.split("|", 1)
            lignes_struct.append("#Q" + "#" * 54)
            lignes_struct.append(q.strip())
            lignes_struct.append("#A" + "-" * 54)
            lignes_struct.append(f"#-[type:text] {a.strip()} -#")
        else:
            lignes_struct.append(ligne)
    return lignes_struct

def convertir_docx_en_txt(docx_path: Path):
    nom_fichier = docx_path.stem
    code = "-".join(nom_fichier.split("-")[:3])

# Définition du chemin de log pour ce fichier
    log_path = output_dir / "log" / f"log_{code}.txt"
    log_path.parent.mkdir(parents=True, exist_ok=True)  # S'assurer que le dossier existe


    file_date = datetime.fromtimestamp(docx_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    images_dir = output_dir / "images"
    doc = Document(docx_path)

    # === EXTRACTION PHYSIQUE DES IMAGES ===
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    from io import BytesIO
    from hashlib import md5

    image_hash_map = {}
    image_names_used = []  # liste ordonnée d'utilisation des images
    image_number = 1
    image_filenames_in_order = []  # ordre réel d'utilisation

    for rel in doc.part._rels.values():
        if rel.reltype == RT.IMAGE:
            img_data = rel.target_part.blob
            img_hash = md5(img_data).hexdigest()

            if img_hash not in image_hash_map:
                ext = rel.target_part.content_type.split("/")[-1]
                img_name = f"{code}_image{image_number:03}.{ext}"
                img_path = images_dir / img_name
                with open(img_path, "wb") as img_out:
                    img_out.write(img_data)
                image_hash_map[img_hash] = img_name
                image_filenames_in_order.append(img_name)
                image_number += 1
    blocs = []
    image_counter = 1
    auteur = "MC"

#    for para in doc.paragraphs:
#        drawings = para._element.xpath('.//w:drawing')
#        text = para.text.strip()
#        has_image = bool(drawings)
#
#        block = ""
#        if text:
#            block += text
#        if has_image:
#            image_names_used.append(f"{nom_fichier}_image{image_counter:03}.png")
#            blocs.append(block)
## image_name déjà défini via image_hash_map
#            if image_counter <= len(image_filenames_in_order):
#                img_name_ref = image_filenames_in_order[image_counter - 1]
#            else:
#                img_name_ref = "image_inconnue.png"  # sécurité
#
#            blocs.append(f"#PICT{image_counter:03}# [image: {img_name_ref}]")
#            print(f"📌 Balise image : {img_name_ref}")
#            image_counter += 1
#        elif text:
#            blocs.append(block)
#        else:
#            blocs.append(text)


    image_ref_index = 0  # 🆕 index pour suivre la position dans image_filenames_in_order

    for para in doc.paragraphs:
        drawings = para._element.xpath('.//w:drawing')
        text = para.text.strip()
        has_image = bool(drawings)

        block = ""
        if text:
            block += text

        if has_image:
            image_names_used.append(f"{nom_fichier}_image{image_counter:03}.png")
            blocs.append(block)

            # 🔁 Obtenir le bon nom d’image extrait
            if image_ref_index < len(image_filenames_in_order):
                img_name_ref = image_filenames_in_order[image_ref_index]
            else:
                img_name_ref = "image_inconnue.png"

            blocs.append(f"#PICT{image_counter:03}# [image: {img_name_ref}]")

            print(f"📌 Balise image : {img_name_ref}")

            image_counter += 1
            image_ref_index += 1

        elif text:
            blocs.append(block)
        else:
            blocs.append(text)


    new_blocs = []
    skip_next = False
    for ligne in blocs:
        if skip_next:
            skip_next = False
            continue
        if ligne.lower() == "défi":
            skip_next = True
            continue
        if "|" in ligne and ligne.lower().startswith("défi"):
            parts = ligne.split("|")
            if len(parts) == 2 and parts[1].strip().isalpha():
                auteur = parts[1].strip()
                continue
        new_blocs.append(ligne)
    blocs = new_blocs

# Affichage complet de toutes les lignes lues depuis le document
    print("\n=== 🧾 Contenu complet des blocs lus depuis le document ===")
    for i, line in enumerate(blocs, 1):
        print(f"{i:03} | {line}")
    print("=== Fin des blocs ===\n")




    split_index = next((i for i, line in enumerate(blocs) if 'Herausforderung' in line), len(blocs))
    blocs_fr = blocs[:split_index]
##    blocs_de = [line for line in blocs[split_index:] if not line.strip().startswith('Herausforderung')]
##
##    fr_header, fr_footer = get_struct("fr", nom_fichier, code, auteur, file_date)
##    de_header, de_footer = get_struct("de", nom_fichier, code, auteur, file_date)
##
##    txt_path = output_dir / f"{nom_fichier}.txt"
##    txt_path.write_text(
##        "\n".join(fr_header + process_blocs(blocs_fr) + fr_footer + [""] +
##                              de_header + process_blocs(blocs_de) + 
##                              de_footer +
##                                ["", "## Images"]
##                    ),
##        encoding="utf-8"
##   )
##    input("🔎 Pause — appuyez sur Entrée pour continuer...")


    # === DÉCOUPAGE MULTILINGUE (FR / DE / IT) ===

    # 🔍 Vérification de l'unicité des marqueurs
    def check_unique_marker(blocs, marqueur, nom_fichier, log_path):
        count = sum(1 for line in blocs if marqueur in line)
        if count > 1:
            print(f"❌ Erreur : le mot-clé '{marqueur}' apparaît {count} fois dans {nom_fichier}")
            with open(log_path, "a", encoding="utf-8") as log:
                log.write(f"{nom_fichier} : NOT OK - mot-clé '{marqueur}' apparaît {count} fois\n")
            return False
        return True

    # Vérifications
    if not check_unique_marker(blocs, "Herausforderung", nom_fichier, log_path):
        return
    if not check_unique_marker(blocs, "Sfida", nom_fichier, log_path):
        return

    # Indices de découpe
    idx_de = next((i for i, line in enumerate(blocs) if 'Herausforderung' in line), len(blocs))
    idx_it = next((i for i, line in enumerate(blocs) if 'Sfida' in line), len(blocs))

    # Séparation des blocs
    blocs_fr = blocs[:idx_de]
    blocs_de = blocs[idx_de:idx_it] if idx_de < idx_it else []
    blocs_it = blocs[idx_it:] if idx_it < len(blocs) else []

    # Nettoyage des marqueurs
    blocs_de = [line for line in blocs_de if not line.strip().startswith('Herausforderung')]
    blocs_it = [line for line in blocs_it if not line.strip().startswith('Sfida')]

    # Réinitialisation du compteur à chaque langue
    image_counter = 1
    fr_header, fr_footer = get_struct("fr", nom_fichier, code, auteur, file_date)
    bloc_fr = fr_header + process_blocs(blocs_fr) + fr_footer + [""]

    if blocs_de:
        image_counter = 1
        de_header, de_footer = get_struct("de", nom_fichier, code, auteur, file_date)
        bloc_de = de_header + process_blocs(blocs_de) + de_footer + [""]
    else:
        bloc_de = []

    if blocs_it:
        image_counter = 1
        it_header, it_footer = get_struct("it", nom_fichier, code, auteur, file_date)
        bloc_it = it_header + process_blocs(blocs_it) + it_footer + [""]
    else:
        bloc_it = []

    # Écriture du fichier final
    txt_path = output_dir / f"{nom_fichier}.txt"
    txt_path.write_text(
        "\n".join(bloc_fr + bloc_de + bloc_it + ["## Images"]),
        encoding="utf-8"
    )

    input("🔎 Pause — appuyez sur Entrée pour continuer...")

##

    log_path = log_dir / f"{nom_fichier}.log"
    with open(log_path, "w", encoding="utf-8") as logf:
        logf.write(f"# Script : {SCRIPT_NAME}\n")
        logf.write(f"# Execution Time : {TIMESTAMP}\n")
        logf.write("# ==========================================\n")
        logf.write(f"Fichier : {docx_path.name}\n")
        logf.write(f"Paragraphes : {len(doc.paragraphs)}\n")
        logf.write(f"Images extraites : {image_counter - 1}\n")


    # Réorganisation des images : les collecter et les placer après ## Images
    with open(txt_path, "r", encoding="utf-8") as fin:
        lines_txt = fin.readlines()

    content_without_images = []
    image_blocks = []
    image_log = {"fr": [], "de": []}
    current_lang = "fr"
    current_question = None
    i = 0

    while i < len(lines_txt):
        line = lines_txt[i]
        if line.strip().startswith("\f"):
            current_lang = "de"
        if line.strip().startswith("#Q"):
            # ligne suivante est la question → capture identifiant
            current_question = lines_txt[i + 1].strip()
        if line.strip().startswith("#PICT") and i + 1 < len(lines_txt) and lines_txt[i + 1].strip().startswith("[image:"):
            image_blocks.append(lines_txt[i])
            image_blocks.append(lines_txt[i + 1])
            image_log[current_lang].append(f"{current_question}  {lines_txt[i + 1].strip()}")
            i += 2
            continue
        else:
            content_without_images.append(line)
            i += 1

    # vérification de synchronisation des images
    status = "OK"
    if len(image_log["fr"]) != len(image_log["de"]):
        status = "NOT OK"

    # réécriture avec repositionnement
    final_output = []
    for line in content_without_images:
        final_output.append(line)
        if line.strip() == "## Images":
            final_output.append("\n")
            final_output.extend(image_blocks)

    with open(txt_path, "w", encoding="utf-8") as fout:
        fout.writelines(final_output)

    # journalisation image/log individuel
    with open(log_path, "a", encoding="utf-8") as logf:
        logf.write("\n-- Images intégrées --\n")
        logf.write("Français\n")
        for l in image_log["fr"]:
            logf.write(f"{l}\n")
        logf.write("Allemand\n")
        for l in image_log["de"]:
            logf.write(f"{l}\n")

    # Réorganisation des images : repositionnement après ## Images
    with open(txt_path, "r", encoding="utf-8") as fin:
        lines_txt = fin.readlines()

    content_without_images = []
    image_blocks = []
    image_log = {"fr": [], "de": []}
    current_lang = "fr"
    current_question = None
    i = 0

    while i < len(lines_txt):
        line = lines_txt[i]

        if line.strip().startswith("\f"):
            current_lang = "de"

        if line.strip().startswith("#Q") and i + 1 < len(lines_txt):
            current_question = lines_txt[i + 1].strip()

        if line.strip().startswith("#PICT") and i + 1 < len(lines_txt) and lines_txt[i + 1].strip().startswith("[image:"):
            image_blocks.append(line)
            image_blocks.append(lines_txt[i + 1])
            image_log[current_lang].append(f"{current_question}  {lines_txt[i + 1].strip()}")
            i += 2
            continue

        content_without_images.append(line)
        i += 1

    # Évaluation de synchronisation
    status = "OK"
    if len(image_log["fr"]) != len(image_log["de"]):
        status = "NOT OK"

    # Réécriture du fichier avec images déplacées
    final_output = []
    for line in content_without_images:
        final_output.append(line)
        if line.strip() == "## Images":
            final_output.append("\n")
            final_output.extend(image_blocks)

    with open(txt_path, "w", encoding="utf-8") as fout:
        fout.writelines(final_output)

    # Log individuel des images
    with open(log_path, "a", encoding="utf-8") as logf:
        logf.write("\n-- Images intégrées --\n")
        logf.write("Français\n")
        for l in image_log["fr"]:
            logf.write(f"{l}\n")
        logf.write("Allemand\n")
        for l in image_log["de"]:
            logf.write(f"{l}\n")
    return nom_fichier

global_log = log_dir / "_global_extraction.log"
with open(global_log, "w", encoding="utf-8") as f:
    f.write(f"# Script : {SCRIPT_NAME}\n")
    f.write(f"# Execution Time : {TIMESTAMP}\n")
    f.write("# ==========================================\n")
    for fichier in files:
        nom = convertir_docx_en_txt(fichier)
        f.write(f"{nom} : OK\n")

# print("=== Résultat du traitement ===")
# for fichier in files:
#    try:
#        nom = convertir_docx_en_txt(fichier)
#        print(f"{nom} : OK")
#    except Exception as e:
#        print(f"{fichier.stem} : NOT OK - {str(e)}")

# Boucle principale – traitement de tous les fichiers .docx
fichiers = list(input_dir.glob("*.docx"))

for fichier in fichiers:
    print(f"🔄 Traitement : {fichier.name}")
    nom = convertir_docx_en_txt(fichier)

    if nom is None:
        print(f"❌ Fichier ignoré suite à une erreur détectée : {fichier.name}")
        continue  # Ne pas aller plus loin si erreur fatale

    print(f"{nom} : OK")
