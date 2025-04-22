# 📘 Sauvegarde de la documentation dans Git

Ce fichier rappelle les commandes à utiliser pour versionner et sauvegarder proprement les fichiers `.md` du dossier `docs/`.

---

## ✅ Étapes de base

### 1. Ajouter tous les fichiers `.md` modifiés ou créés :
```bash
git add docs/*.md
```

### 2. Faire un commit avec un message clair :
```bash
git commit -m "Mise à jour documentation – structure_projet, suivi, etc."
```

### 3. Pousser les changements vers le dépôt distant :
```bash
git push
```

---

## ✅ Résumé

git add docs/*.md
git commit -m "Mise à jour documentation – structure_projet, suivi, etc."
git push

---

## 🔖 Créer un tag spécifique pour une version de documentation

### 4. Ajouter un tag :
```bash
git tag doc-v1.01
```

### 5. Pousser le tag :
```bash
git push origin doc-v1.01
```

---

## 🔁 Mais au fait… c’est quoi `origin` ?

### 🧠 `origin` = le nom par défaut donné au **dépôt distant GitHub** lorsque tu as cloné le projet.

Quand tu fais :
```bash
git push origin <branche-ou-tag>
```
Cela veut dire :
> "Envoie cette branche ou ce tag vers le dépôt distant nommé `origin`" (en général : ton dépôt GitHub)

Tu peux voir à quoi `origin` correspond avec :
```bash
git remote -v
```

Cela affichera l’adresse exacte du dépôt GitHub auquel `origin` est lié.

---

