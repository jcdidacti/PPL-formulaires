# ============================================================================
# Script : passe1_v2_balises_etape2.py
# Objectif : Étape 2 — corriger en-tête, normaliser #ID/#Author, insérer ##Introduction + ##Work Start si absents
# ============================================================================
import re
import shutil
from pathlib import Path
from docx import Document
from datetime import datetime
from zipfile import ZipFile

VERSION_SCRIPT = "v2.0-etape2"
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

def detect_lang(text):
    if "Herausforderung" in text or "Antwort" in text:
        return "de"
    return "fr"

def extraire_images(docx_path, base_name):
    docx_zip = ZipFile(docx_path)
    count, liens, trouvées = 1, {}, []
    from xml.etree.ElementTree import fromstring as fs
    rels = fs(docx_zip.read("word/_rels/document.xml.rels"))
    for r in rels:
        if "Id" in r.attrib and "Target" in r.attrib:
            liens[r.attrib["Id"]] = r.attrib["Target"]
    contenu = docx_zip.read("word/document.xml").decode("utf-8")
    cibles = re.findall(r'(<a:blip.+?r:embed="(rId\d+)"[^>]*/>)', contenu)
    lignes = []
    for bloc, rId in cibles:
        target = liens.get(rId, "")
        if not target.lower().startswith("media/"):
            continue
        nom_image = target.split("/")[-1]
        suffix = Path(nom_image).suffix.lower()
        if suffix not in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]:
            continue
        tag = f"#PICT{count:03}# [image: {base_name}_image{count:03}{suffix}]"
        lignes.append(tag)
        with docx_zip.open("word/" + target) as src, open(image_dir / f"{base_name}_image{count:03}{suffix}", "wb") as dest:
            shutil.copyfileobj(src, dest)
        count += 1
    return lignes

def corriger_bloc_langue(bloc):
    nouvelles_lignes = []
    introduit_intro = False
    for i, ligne in enumerate(bloc):
        l = ligne.strip()
        if l.startswith("ID "):
            l = "#ID" + l[2:]
        elif l.startswith("Version "):
            l = "#Version" + l[7:]
        elif l.startswith("Date "):
            l = "#Date" + l[4:]
        elif l.startswith("Auteur") or l.startswith("#Auteur"):
            l = "#Author" + l[len("Auteur"):] if "Auteur" in l else "#Author" + l[len("#Auteur"):]
        nouvelles_lignes.append(l)
        if l.startswith("#Author") and not introduit_intro:
            nouvelles_lignes.append("")
            nouvelles_lignes.append("##Introduction")
            nouvelles_lignes.append("[texte d’introduction]")
            nouvelles_lignes.append("")
            nouvelles_lignes.append("##Work Start")
            introduit_intro = True
    return nouvelles_lignes

def traiter_fichier(docx_path):
    base_name = docx_path.stem
    doc = Document(docx_path)
    contenu = [p.text.strip() for p in doc.paragraphs if p.text.strip() != ""]
    texte_brut = "\n".join(contenu)
    langue = detect_lang(texte_brut)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.now().strftime("%Y-%m-%d")
    en_tete = ["##Identification", f"#Script : passe1_v2_balises_etape2.py", f"#Run at : {now}", f"#ID file : {base_name}", f"##LANG-{langue}"]
    bloc_corrige = corriger_bloc_langue(contenu)
    final = en_tete + [""] + bloc_corrige + ["", "##Work End", "##Form End"]
    final += ["", "# Images extraites"] + extraire_images(docx_path, base_name)
    sortie = output_dir / f"{base_name}.txt"
    sortie.write_text("\n".join(final), encoding="utf-8")
    global_log_entries.append(f"{base_name} : OK")
    print(f"✔ Généré : {base_name}.txt")

if __name__ == "__main__":
    fichiers = list(input_dir.glob("*.docx"))
    for fichier in fichiers:
        if fichier.name.startswith("~$"):
            continue
        traiter_fichier(fichier)
    with open(global_log_path, "w", encoding="utf-8") as f:
        f.write(f"# Global log — passe1 (version : {VERSION_SCRIPT})\n")
        f.write(f"# Run : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("# ===========================================\n")
        for entry in global_log_entries:
            f.write(entry + "\n")
