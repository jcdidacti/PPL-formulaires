# 🚀 Démarrage d'une nouvelle passe de traitement

Ce fichier sert de guide pour structurer chaque nouvelle étape (passe) du projet `PPL-formulaires`.

---

## 🧠 Objectif de la passe

> Expliquer en quelques phrases ce que cette passe est censée faire (analyse, transformation, extraction, etc.)

---

## 📥 Entrée(s)

- Type de fichier(s) attendus :
- Emplacement : `<base>/data/...`

---

## 📤 Sortie(s)

- Type de fichiers produits :
- Emplacement : `<base>/data/...`

---

## 📂 Répertoires à créer si nécessaires

```
<base>/data/XX...
├── ...
└── ...
```

---

## 🛠️ Script associé

- Nom du fichier : `passeX_nom_de_la_passe.py`
- Emplacement : `scripts/`
- Nom du tag attendu : `passeX-vX.XX`

---

## 🧪 Exemple concret – (à adapter)

### Objectif :
Reformuler les questions d’un fichier `.txt` en questions ouvertes, tout en identifiant les balises de réponse et en les typant.

### Entrée :
```
<base>/data/02text_p1_out/
→ Fichiers `.txt` générés par passe1
```

### Sortie :
```
<base>/data/03text_p2_out/
→ Fichiers `.txt` avec reformulation
→ Log de traitement
```

### Script :
- `scripts/passe2_txt_to_reformulated.py`
- Tag : `passe2-v2.00`

---

🧭 À remplir à chaque nouvelle passe pour garder la vision claire du projet.
