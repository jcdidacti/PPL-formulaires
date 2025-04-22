# 🌍 Convention multilingue – Projet PPL-formulaires

Ce document définit les règles de structuration et de traitement des questionnaires multilingues dans le projet.

---

## 📐 Structure d'un fichier multilingue

Un fichier peut contenir plusieurs langues dans l'ordre :

- 🇫🇷 **Français** (aucun mot-clé requis)
- 🇩🇪 **Allemand** → détecté par la présence du mot-clé **"Herausforderung"**
- 🇮🇹 **Italien** → détecté par la présence du mot-clé **"Sfida"**

Chaque bloc est séparé selon ces mots-clés et traité indépendamment.

---

## ⚙️ Fonctionnement du script

### 1. Le script détecte chaque langue en cherchant les mots-clés dans l’ordre :
- "Herausforderung"
- "Sfida"

### 2. Il découpe le fichier `.docx` en trois sections :
- `blocs_fr`, `blocs_de`, `blocs_it`

### 3. À chaque langue :
- Le compteur d’images `image_counter` est réinitialisé à 1
- Les balises `#PICTnnn# [image: ...]` sont générées proprement
- Un en-tête et un pied-de-page sont ajoutés avec `get_struct(...)`

### 4. En cas d’erreur :
- Si un mot-clé apparaît **plus d'une fois**, le traitement s'arrête
- L’erreur est enregistrée dans le fichier log avec la mention `NOT OK`

---

## 🔍 Exemple de balises générées

Dans le fichier `.txt` final :

```text
#PICT001# [image: 00-2-04_image001.png]
#PICT002# [image: 00-2-04_image002.png]
...
#PICT001# [image: 00-2-04_image001.png]  ← redémarre pour l'allemand
...
```

---

## ✅ Avantages de cette convention

- Prévisible et extensible à d'autres langues
- Traitable automatiquement
- Compatible avec les logs, balises et formats futurs

---

📌 À maintenir à jour si de nouveaux marqueurs ou langues sont ajoutés.
