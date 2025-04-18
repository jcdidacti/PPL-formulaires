# 📁 Structure du projet PPL-formulaires

Ce fichier documente la structure des dossiers utilisés pour chaque étape de traitement par script (passes).

---

## 🗂️ Arborescence du projet

```
PPL-formulaires/
├── data/
│   ├── 00docx_tab/              ← fichiers .docx d’origine sous forme de tableau
│   ├── 01docx_lin_in/           ← fichiers linéarisés générés par passe0
│   │   └── log/                 ← journaux de traitement de passe0
│   ├── 02docx_lin_out/          ← fichiers .docx nettoyés, validés pour extraction
│   └── 02text_p1_out/           ← fichiers .txt issus de l’extraction par passe1
│       ├── images/              ← images extraites des docx
│       └── log/                 ← journaux de traitement de passe1
├── scripts/
│   ├── passe0_docx_tab_to_lin.py
│   └── passe1_docx_lin_to_txt.py
├── docs/
│   ├── structure_projet.md
│   └── ...
├── .gitignore
└── README.md
```

---

## ✅ Passe 0 : `passe0_docx_tab_to_lin.py`

### 📄 Emplacement du script :
```
<base>/scripts/passe0_docx_tab_to_lin.py
```

### 📥 Lecture :
```
<base>/data/00docx_tab/
→ Fichiers .docx d’origine sous forme de tableaux (documents bruts)
```

### 📤 Écriture :
```
<base>/data/01docx_lin_in/
→ Fichiers .docx linéarisés (conversion automatique depuis tableaux)

<base>/data/01docx_lin_in/log/
→ Logs de traitement associés aux fichiers linéarisés
```

### Remarques :
- Tous les chemins sont relatifs à la racine du projet (`<base>`)
- La structure est conçue pour faciliter l’automatisation, le versionnage, et la lisibilité
- Le dossier `data/` centralise toutes les données de travail

---

🧩 Les autres passes (passe1, passe2a, etc.) seront ajoutées progressivement.
---

## ✅ Passe 1 : `passe1_docx_lin_to_txt.py`

### 📄 Emplacement du script :
```
<base>/scripts/passe1_docx_lin_to_txt.py
```

### 📥 Lecture :
```
<base>/data/02docx_lin_out/
→ Fichiers .docx linéaires revus manuellement (préparés pour extraction de contenu)
```

### 📤 Écriture :
```
<base>/data/02text_p1_out/
→ Fichiers texte `.txt` générés automatiquement depuis les fichiers .docx

<base>/data/02text_p1_out/images/
→ Images extraites des fichiers docx (référencées dans les textes)

<base>/data/02text_p1_out/log/
→ Journaux de traitement de passe1 (résumés, erreurs, diagnostics)
```

### Remarques :
- Cette passe effectue l'extraction structurée du contenu linéaire + des images
- Les fichiers générés seront utilisés dans les passes suivantes pour reformulation, syntaxe, etc.
- Tous les chemins sont relatifs à la racine du projet, regroupés dans `data/`
