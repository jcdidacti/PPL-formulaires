# ============================================================================
# Script : passe1_v2_balises.py
# Objectif : Générer un .txt structuré (balises.md) à partir d’un .docx linéaire avec images
# Date : 2025-05-01
# ============================================================================
import re
from docx import Document
from pathlib import Path
import shutil
from datetime import datetime
from zipfile import ZipFile
import xml.etree.ElementTree as ET

base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
input_dir = data_dir / "02docx_lin_out"
output_dir = data_dir / "02text_p1_out"
image_dir = output_dir / "images"
log_dir = output_dir / "log"
output_dir.mkdir(parents=True, exist_ok=True)
image_dir.mkdir(parents=True, exist_ok=True)
log_dir.mkdir(parents=True, exist_ok=True)

def extract_images(docx_path, base_name):
    img_output = []
    with ZipFile(docx_path, 'r') as zipf:
        rels = ET.fromstring(zipf.read('word/_rels/document.xml.rels'))
        rels_dict = {r.attrib['Id']: r.attrib['Target'] for r in rels if 'Target' in r.attrib}
        doc = ET.fromstring(zipf.read('word/document.xml'))
        count = 1
        for blip in doc.findall('.//a:blip', {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}):
            rId = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if rId in rels_dict:
                img_path = 'word/' + rels_dict[rId]
                ext = Path(img_path).suffix.lower()
                if ext in [".png", ".jpg", ".jpeg", ".gif", ".bmp"]:
                    dest_name = f"{base_name}_image{count:03}{ext}"
                    with zipf.open(img_path) as src, open(image_dir / dest_name, 'wb') as dst:
                        shutil.copyfileobj(src, dst)
                    img_output.append(f"#PICT{count:03}# [image: {dest_name}]")
                    count += 1
    return img_output

def detect_lang(text):
    if "Herausforderung" in text or "Antwort" in text:
        return "de"
    return "fr"

def process_docx(docx_path):
    base_name = docx_path.stem
    doc = Document(docx_path)
    full_text = [p.text.strip() for p in doc.paragraphs if p.text.strip() != ""]
    joined = "\n".join(full_text)
    lang = detect_lang(joined)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.now().strftime("%Y-%m-%d")
    head = ["##Identification", f"#Script : passe1_v2_balises.py", f"#Run at : {now}", f"#ID file : {base_name}", f"##LANG-{lang}", "#ID        XX-X-XX", "#Version   1.00", f"#Date      {today}", "#Author    ...", "", "##Introduction", "[texte d’introduction]", "", "##Work Start"]
    result = head + [""] + full_text + ["", "##Work End", "##Form End"]
    out_path = output_dir / f"{base_name}.txt"
    pict_tags = extract_images(docx_path, base_name)
    if pict_tags:
        result.append("")
        result.append("# Images extraites")
        result.extend(pict_tags)
    out_path.write_text("\n".join(result), encoding="utf-8")
    print(f"✔ Généré : {out_path.name}")

if __name__ == "__main__":
    docx_files = list(input_dir.glob("*.docx"))
    for docx_path in docx_files:
        process_docx(docx_path)
