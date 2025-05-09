# ==============================================================================
# Script : build_referentiel.py
# Objectif : Générer un fichier de référence global à partir des fichiers ref_*.md
# Date : 2025-05-09
# ==============================================================================

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Génère le fichier ref_ppl_process_global.md à partir des documents ref_*.md"
)
parser.add_argument(
    "--full", action="store_true",
    help="Inclure également le contenu des fichiers de changelog (ref_*.md secondaires)"
)

args = parser.parse_args()

base_dir = Path(__file__).resolve().parent.parent / "docs"

ref_files = [
    "ref_methodo.md",
    "ref_passe0.md",
    "ref_passe1.md",
    "ref_passe2.md",
    "ref_balises.md"
]

sections = []
toc_lines = []
print("\n📚 Construction du référentiel global (ref_ppl_process_global.md)\n")

for ref in ref_files:
    ref_path = base_dir / ref
    section_title = f"# {ref.replace('.md', '')}"
    anchor = ref.replace(".md", "").lower()
    toc_lines.append(f"- [{ref}](#{anchor})")

    if ref_path.exists():
        print(f"✅ {ref} chargé")
        content = ref_path.read_text(encoding="utf-8")

        suffix = ref.replace(".md", "_")
        subrefs = sorted(base_dir.glob(f"{suffix}*.md"))
        sub_citations = ""
        full_sub_content = []

        for sref in subrefs:
            if sref.name != ref:
                print(f"\t{sref.name} cité")
                sub_citations += f"📎 {sref.name}\n"
                if args.full:
                    full_sub_content.append(f"### {sref.name}\n\n" + sref.read_text(encoding="utf-8").strip())

        header = f"<a name=\"{anchor}\"></a>\n\n# {ref}\n\n{section_title}\n\n"
        if sub_citations:
            header += f"**Fichiers associés :**\n{sub_citations}\n"
        if full_sub_content:
            header += "\n\n" + "\n\n---\n\n".join(full_sub_content)

        sections.append(header + content.strip())
    else:
        print(f"⚠️ Manquant : {ref}")
        sections.append(f"<a name=\"{anchor}\"></a>\n\n⚠️ Fichier manquant : {ref}\n\n---")

# Table des matières
toc = "# 📑 Table des matières\n\n" + "\n".join(toc_lines)

# Finalisation
full_content = toc + "\n\n" + "\n\n---\n\n".join(sections)
synthese_path = base_dir / "ref_ppl_process_global.md"
synthese_path.write_text(full_content, encoding="utf-8")

print(f"\n✅ Fichier généré : {synthese_path.name}\n")

# === Options CLI ===

Ce script accepte les options suivantes :

- `--help` : affiche cette aide
- `--full` : inclut également le contenu des fichiers de changelog (ref_passe0_2.xx.md, etc.)