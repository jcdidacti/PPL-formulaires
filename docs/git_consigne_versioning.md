
# 📘 Consignes de versioning – Projet PPL-formulaires

Ce fichier contient les bonnes pratiques et commandes utiles pour suivre les versions des scripts, notamment ceux liés à la `passe1`.

---

## 🏷️ Convention de nommage des tags

- `passe0-vX.XX` → transformation tableau → linéaire
- `passe1-vX.XX` → transformation linéaire → .txt avec images
- `session-YYYY-MM-DD-HHhMM` → sauvegarde ponctuelle manuelle

---

## ✅ Bonnes pratiques

- Chaque version validée doit être copiée dans `passe1_docx_lin_to_txt.py`
- Le tag correspondant doit être ajouté et pushé :

```bash
git add scripts/passe1_docx_lin_to_txt.py
git commit -m "passe1 v2.69 – gestion des images - version beta"
git tag passe1-v2.69
git push
git push origin passe1-v2.69
```

---

## 🔍 Vérification de l’historique des versions `passe1-v*.*`

### 1. Lister tous les tags `passe1-v*.*` triés par date
```bash
git tag --list "passe1-v*.*" --sort=taggerdate
```

### 2. Voir les messages de commit associés à chaque tag
```bash
for t in $(git tag --list "passe1-v*.*" --sort=taggerdate); do
    git show $t --no-patch --oneline
done
```

### 3. Rechercher tous les commits contenant "passe1" dans leur message
```bash
git log --oneline --grep="passe1"
```

### 4. Voir les commits et leurs tags (vue synthétique)
```bash
git log --oneline --decorate
```

---

📌 Pensez à garder ce fichier à jour en cas d'ajout d'autres branches de développement.
