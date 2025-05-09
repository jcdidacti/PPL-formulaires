import hashlib
import sys
from pathlib import Path

def get_file_hash(path):
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def main(file1, file2):
    path1 = Path(file1)
    path2 = Path(file2)

    if not path1.exists() or not path2.exists():
        print("❌ Un ou les deux fichiers n'existent pas.")
        return

    hash1 = get_file_hash(path1)
    hash2 = get_file_hash(path2)

    if hash1 == hash2:
        print("✅ Les fichiers sont strictement identiques.")
    else:
        print("❗ Les fichiers sont différents.")
        print(f"{file1} → {hash1}")
        print(f"{file2} → {hash2}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python compare_files.py chemin/fichier1 chemin/fichier2")
    else:
        main(sys.argv[1], sys.argv[2])
