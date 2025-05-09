
import argparse
import shutil
from pathlib import Path
import sys

def archiver_fichier(filename, prefix):
    base_docs = Path(__file__).parent.parent / "docs"
    source = base_docs / filename

    if not source.exists():
        print(f"❌ Erreur : le fichier '{source}' n'existe pas.")
        sys.exit(1)

    if not prefix:
        print("❌ Erreur : un préfixe est obligatoire (exemples valides : old_, legacy_, archive_, vYYYY-MM-DD_).")
        sys.exit(1)

    archive_dir = base_docs / "archive"
    archive_dir.mkdir(exist_ok=True)

    destination = archive_dir / f"{prefix}{source.name}"

    shutil.move(str(source), str(destination))
    print(f"✅ Fichier archivé avec succès : {destination}")

def main():
    parser = argparse.ArgumentParser(
        description="""
Archiver un fichier présent dans 'docs/' en lui ajoutant un préfixe obligatoire.

Exemples de préfixes :
  - old_       → ancienne version simple
  - legacy_    → format obsolète mais conservé
  - archive_   → version déplacée sans remplaçant
  - v2025-04-25_ → version datée
""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--file", required=True, help="Nom du fichier dans 'docs/' à archiver (ex: bloc_notes.md)")
    parser.add_argument("--prefix", required=True, help="Préfixe obligatoire pour l'archive (ex: old_, legacy_, archive_)")

    args = parser.parse_args()

    archiver_fichier(args.file, args.prefix)

if __name__ == "__main__":
    main()
