
# ==============================================================================
# Script : passe1_docx_lin_to_txt_v2_60.py
# Objectif : version stable avec balises Q/A et log global
# Date : 2025-04-20
# ==============================================================================

import os
from pathlib import Path
from docx import Document
from hashlib import md5
from datetime import datetime
from docx.opc.constants import RELATIONSHIP_TYPE as RT

# === INIT RÉPERTOIRES ===
base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"

input_dir = data_dir / "02docx_lin_out"
output_dir = data_dir / "02text_p1_out"
image_dir = output_dir / "images"
log_dir = output_dir / "log"

output_dir.mkdir(parents=True, exist_ok=True)
image_dir.mkdir(parents=True, exist_ok=True)
log_dir.mkdir(parents=True, exist_ok=True)

global_log_path = log_dir / "_global_extraction.log"
global_log_entries = []

# === STRUCTURE HEADER/FOOTER ===
def get_struct(nom_fichier, code, auteur):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = [
        "## Identification",
        f"#Script : passe1_docx_lin_to_txt_v2_60.py",
        f"#Run at : {now}",
        f"#ID file : {nom_fichier}",
        f"ID        {code}",
        f"Version   00.00",
        f"Date      20-01-2025",
        f"Auteur    {auteur}",
        "",
        "## Introduction",
        "# To be completed",
        "",
        "## Work Start"
    ]
    footer = [
        "",
        "## Work Stop",
        "",
        "## Personal data",
        "Temps passé sur ce questionnaire :",
        "Code de l'élève :",
        "Code de vérification :",
        "## End of Form"
    ]
    return header, footer

# === TRAITEMENT PRINCIPAL ===
def process_docx(docx_path: Path):
    nom_fichier = docx_path.stem
    code = "-".join(nom_fichier.split("-")[:3])
    auteur = "MC"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"🔍 Traitement : {nom_fichier}")

    doc = Document(docx_path)

    image_hash_map = {}
    image_counter = 1
    bloc_texte = []

    # ========== Extraction unique des images ==========
    for rel in doc.part._rels.values():
        if rel.reltype == RT.IMAGE:
            img_data = rel.target_part.blob
            img_hash = md5(img_data).hexdigest()
            if img_hash not in image_hash_map:
                ext = rel.target_part.content_type.split("/")[-1]
                img_name = f"{code}_image{image_counter:03}.{ext}"
                img_path = image_dir / img_name
                with open(img_path, "wb") as f:
                    f.write(img_data)
                image_hash_map[img_hash] = img_name
                image_counter += 1

    image_counter = 1
    image_list = list(image_hash_map.values())

    try:
        for para in doc.paragraphs:
            drawings = para._element.xpath('.//w:drawing')
            text = para.text.strip()
            has_image = bool(drawings)

            # Détection auteur
            if "défi" in text.lower() and "|" in text:
                parts = text.split("|")
                if len(parts) == 2 and parts[1].strip():
                    auteur = parts[1].strip()
                    continue

            if "|" in text:
                q, a = text.split("|", 1)
                bloc_texte.append("#Q######################################################")
                bloc_texte.append(q.strip())
                bloc_texte.append("#A------------------------------------------------------")
                bloc_texte.append(f"#-[type:text] {a.strip()} -#")
            elif text:
                bloc_texte.append(text)

            if has_image:
                img_name = image_list[image_counter - 1] if image_counter <= len(image_list) else "image_inconnue.png"
                bloc_texte.append(f"#PICT{image_counter:03}# [image: {img_name}]")
                image_counter += 1

        header, footer = get_struct(nom_fichier, code, auteur)
        final_content = header + bloc_texte + footer + ["", "## Images"]

        txt_path = output_dir / f"{nom_fichier}.txt"
        txt_path.write_text("\n".join(final_content), encoding="utf-8")

        log_path = log_dir / f"{nom_fichier}.log"
        with open(log_path, "w", encoding="utf-8") as logf:
            logf.write(f"# Script : passe1_docx_lin_to_txt_v2_60.py\n")
            logf.write(f"# Execution Time : {timestamp}\n")
            logf.write(f"# File processed : {docx_path.name}\n")
            logf.write(f"# Paragraphs : {len(doc.paragraphs)}\n")
            logf.write(f"# Images extraites : {len(image_list)}\n")

        global_log_entries.append(f"{nom_fichier} : OK")
        return True

    except Exception as e:
        global_log_entries.append(f"{nom_fichier} : NOT OK - {e}")
        return False

# === BOUCLE PRINCIPALE ===
if __name__ == "__main__":
    fichiers = list(input_dir.glob("*.docx"))
    for fichier in fichiers:
        if fichier.name.startswith("~$"):
            print(f"⏭️ Fichier ignoré : {fichier.name}")
            continue
        process_docx(fichier)

    # Log global
    with open(global_log_path, "w", encoding="utf-8") as f:
        f.write("# Global log — passe1 v2.60\n")
        f.write(f"# Run : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("# ===========================================\n")
        for entry in global_log_entries:
            f.write(entry + "\n")
