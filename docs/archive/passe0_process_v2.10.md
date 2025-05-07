# Passe 0 – Conversion Tableau Word → Fichier Linéaire avec Images et Balises

## 🎯 Objectif
Transformer un fichier `.docx` contenant des **tableaux Word** en un fichier `.docx` **linéaire** structuré pour traitement ultérieur, avec :
- Texte des cellules réorganisé ligne à ligne
- Images extraites et référencées
- Balises `#Q#######` et `#A-------` détectées ou insérées automatiquement
- Repères d’images par cellule (`#RC_...`)
- Balises de structure attendues par la passe 1 : `##Identification`, `##Introduction`, `##Work Start`, `##Work End`, `##Form End`

---

## 🧠 Fonctionnement du script `passe0_docx_tab_to_lin_img.py` (version v2.10)

### 1. Initialisation
- Répertoires : `data/00docx_tab` (entrées), `data/01docx_lin_in` (sorties), `images/` et `log/`
- Tous les fichiers `.docx` du dossier d’entrée sont analysés

### 2. Analyse du tableau
- Le tableau est scanné ligne par ligne à partir de la **deuxième ligne** (la première est ignorée)
- La **dernière ligne** est également ignorée (typiquement `Temps passé à ce défi` ou équivalent)
- Chaque ligne utile est considérée comme une paire question/réponse

### 3. Détection de la langue
- Déterminée à partir de la ligne 1 du tableau :
  - `Défi | ...` → `fr`
  - `Herausforderung | ...` → `de`

### 4. Génération de l’en-tête
Ajout automatique en début de chaque langue :
```
##Identification
#Script : passe0_docx_tab_to_lin_img.py
#Run at : [horodatage]
#ID file : [nom_fichier]
##LANG-fr / ##LANG-de
#ID : [extrait du nom de fichier]
#Version :
#Date :
#Author :
##Introduction
##Work Start
```

### 5. Gestion des images
- Les images sont extraites **par cellule**
- Indexation via SHA1 pour éviter les doublons
- Nom des images : `[nomfichier]_image_XXX_Q/R_TY_RX.jpeg`
- Ajout de repères :
```
#RC_table_row_Q
#RC_table_row_R
```

---

## 🧩 Détection ou insertion des balises Q/A

### a. Si les balises existent
- La cellule gauche commence par `#Q`, la droite par `#A` → pas de modification

### b. Si elles sont absentes
- Si les deux cellules sont non vides et sans balises :
  - Ajout de `#Q#######` en début de gauche
  - Ajout de `#A-------` en début de droite

---

## 🔚 Fin de bloc
- Lorsqu’on atteint la dernière ligne du tableau (ignorée), insertion de :
```
##Work End
```
- Si langue = `fr`, on ajoute aussi :
```
[PAGEBREAK]
```

---

## 🧼 Résultat produit
Le document linéaire final :
- Est un `.docx` sans mise en forme
- Contient les blocs Q/R avec balises
- Les repères image par cellule
- L’en-tête structuré attendu par les passes 1 et 2
- Aucun champ SDT
- Aucune suppression de réponse (balisage `#- ... -#` non pris en charge ici)

---

## 🚫 Ce que **ne fait pas** la passe 0
- Pas de transformation en champ SDT
- Pas de masquage des réponses
- Pas de validation pédagogique
- Pas de nettoyage stylistique ou suppression de doublons

Ces tâches sont assurées par la **passe 1** et la **passe 2**.

---

## 📌 Historique
- **v2.04** : insertion conditionnelle des balises
- **v2.10** : insertion systématique des en-têtes, détection de langue par ligne 1, exclusion automatique de la dernière ligne, insertion `#Q/#A` si nécessaire
