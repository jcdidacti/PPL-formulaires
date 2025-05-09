# ============================================================================
# Script : passe1_v2_balises_etape7b.py
# Objectif : Étape 7b — Reconnaître balises #Q####### et #A------- même avec contenu
# ============================================================================
import re
import shutil
from pathlib import Path
from docx import Document
from datetime import datetime
from zipfile import ZipFile

VERSION_SCRIPT = "v2.0-etape7b"
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

def detect_lang_bloc(bloc):
    bloc_txt = "\n".join(bloc).lower()
    if "herausforderung" in bloc_txt or "antwort" in bloc_txt:
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

def normaliser_balises(lignes):
    resultat = []
    for ligne in lignes:
        l = ligne.strip()
        if l.startswith("#Q#######") and len(l) > 9:
            resultat.append("#Q#######")
            resultat.append(l[9:].strip())
        elif l.startswith("#A-------") and len(l) > 9:
            resultat.append("#A-------")
            resultat.append(l[9:].strip())
        else:
            resultat.append(ligne)
    return resultat

def formater_bloc_langue(bloc, base_name, langue, date_now):
    bloc = normaliser_balises(bloc)
    id_extrait = base_name.split('-')[0:3]
    id_code = "-".join(id_extrait) if len(id_extrait) == 3 else "XX-X-XX"
    en_tete = [
        "##Identification",
        f"#Script : passe1_v2_balises_etape7b.py",
        f"#Run at : {date_now}",
        f"#ID file : {base_name}",
        f"##LANG-{langue}",
        f"#ID        {id_code}",
        "#Version   1.00",
        f"#Date      {datetime.now().strftime('%Y-%m-%d')}",
        "#Author    ...",
        "",
        "##Introduction",
        "[texte d’introduction]",
        "##Work Start"
    ]
    contenu = []
    in_answer = False
    buffer = []
    for line in bloc:
        if line.strip() == "#A-------":
            if in_answer and buffer:
                contenu.append("#-[type:text] #-")
                contenu.extend(buffer)
                contenu.append("-#")
                buffer = []
            contenu.append("#A-------")
            in_answer = True
        elif line.strip() == "#Q#######":
            if in_answer and buffer:
                contenu.append("#-[type:text] #-")
                contenu.extend(buffer)
                contenu.append("-#")
                buffer = []
                in_answer = False
            contenu.append("#Q#######")
        elif in_answer:
            buffer.append(line)
        else:
            contenu.append(line)
    if in_answer and buffer:
        contenu.append("#-[type:text] #-")
        contenu.extend(buffer)
        contenu.append("-#")
    return en_tete + [""] + contenu

def séparer_blocs(paragraphes):
    blocs, bloc = [], []
    for ligne in paragraphes:
        if "Défi" in ligne or "Herausforderung" in ligne:
            if bloc:
                blocs.append(bloc)
                bloc = []
        bloc.append(ligne)
    if bloc:
        blocs.append(bloc)
    return blocs

def traiter_fichier(docx_path):
    base_name = docx_path.stem
    doc = Document(docx_path)
    paragraphes = [p.text for p in doc.paragraphs if p.text.strip()]
    blocs = séparer_blocs(paragraphes)
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texte_final = []
    for bloc in blocs:
        langue = detect_lang_bloc(bloc)
        bloc_corr = formater_bloc_langue(bloc, base_name, langue, date_now)
        texte_final.extend(bloc_corr)
        texte_final.append("")
    texte_final += ["##Work End", "##Form End"] + ["", "# Images extraites"] + extraire_images(docx_path, base_name)
    sortie = output_dir / f"{base_name}.txt"
    sortie.write_text("\n".join(texte_final), encoding="utf-8")
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
