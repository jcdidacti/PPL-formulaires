# 🔁 Mémo de reprise de session – Projet PPL-formulaires

Ce fichier résume les étapes essentielles pour reprendre le travail sur le projet après une pause.

---

## ✅ 1. Voir les tags des versions stables
```bash
git tag --list
```
Exemple de sortie :
```
passe0-v1.02
passe1-v2.63
```

---

## 📜 2. Voir l’historique d’un script
```bash
git log -- scripts/passe1_docx_lin_to_txt.py
```
Ou en version simplifiée :
```bash
git log --oneline -- scripts/passe1_docx_lin_to_txt.py
```

---

## 📂 3. Voir les fichiers d’un tag et leur contenu
```bash
git show passe1-v2.63 --name-only
```

Voir le contenu d’un fichier à un tag donné :
```bash
git show passe1-v2.63:scripts/passe1_docx_lin_to_txt.py
```

---

## 🛠️ 4. Travailler sur un script en conversation

Indiquer dans la conversation :
- Le nom du script : `passe1_docx_lin_to_txt.py`
- Le tag de départ : `passe1-v2.63`
- Et la nature de l’évolution souhaitée

---

## 📦 5. Recevoir une nouvelle version depuis l’assistant

- Fichier `.py` ou `.zip` contenant la nouvelle version
- À tester manuellement
- À intégrer dans le dossier `scripts/`

---

## 🧊 6. Geler une nouvelle version stable

```bash
git add scripts/passe1_docx_lin_to_txt.py
git commit -m "Amélioration traitement des images (v2.64)"
git tag passe1-v2.64
git push
git push origin passe1-v2.64
```

---

Conserver ce fichier dans `docs/` pour toute reprise future.
