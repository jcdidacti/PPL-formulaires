
# Synthèse - Passe 0 : Conversion Tableau Word → Fichier Linéaire avec Images et Balises

## Objectif principal
Transformer un fichier `.docx` contenant des **tableaux Word** en un fichier `.docx` **linéaire** structuré, avec :
- Texte des cellules réorganisé en lignes
- Images extraites et référencées
- Balises `#Q#######` et `#A-------` détectées ou insérées automatiquement
- Repères d’images par cellule (`#RC_table_row_Q` / `#RC_table_row_R`)
- Balises de structure pour la passe 1 : `##Identification`, `##Introduction`, `##Work Start`, `##Work End`, `##Form End`

Version de référence : `passe0-v2.04`

---

## 1. Détection de la langue et structure du document
- Détection de la langue par la première ligne du tableau :
  - Si ligne commence par `Défi |` → `langue = fr`
  - Si ligne commence par `Herausforderung |` → `langue = de`
- En-tête automatiquement insérée avec les balises :
  ```
  ##Identification
  #Script : v2.04.py
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

---

## 2. Détection ou insertion automatique des balises `#Q#######` et `#A-------`

### a. Cas avec balises déjà présentes
- Si la cellule de gauche commence par `#Q` et la droite par `#A`, elles sont conservées telles quelles

### b. Cas sans balises explicites
- Si une ligne contient **deux colonnes avec contenu**, et **aucune balise** `#Q` ou `#A` :
  - La balise `#Q#######` est ajoutée au début de la cellule gauche
  - La balise `#A-------` est ajoutée au début de la cellule droite
  - La ligne devient :
    ```
    #Q####### Texte question | #A------- Texte réponse
    ```

---

## 3. Traitement des images
- Images extraites depuis les balises XML internes aux cellules
- Chaque image est enregistrée une seule fois (hash SHA1)
- Nom de fichier d'image : `[prefix]_image_XXX_Q/R_TY_RX.jpeg`
- Repères ajoutés dans le fichier final pour chaque cellule contenant une image :
  ```
  #RC_table_row_Q
  #RC_table_row_R
  ```

---

## 4. Gestion des lignes spéciales
- Si la ligne contient `Temps passé à ce défi` (fr) ou `Für diese Herausforderung aufgewendete Zeit` (de) :
  - La balise `##Work End` est insérée
  - Suivie d’un saut de page `[PAGEBREAK]` (pour les blocs français uniquement)

---

## 5. Format final produit
- Le document final est un `.docx` linéaire contenant :
  - Balises structurantes (#Q, #A, ##Identification, etc.)
  - Texte nettoyé (sauts de ligne multiples réduits)
  - Repères d’image par cellule
  - Aucune mise en forme
  - Aucun champ SDT
  - Images écrites dans un dossier à part `images/`

---

## 6. Ce que la passe 0 **ne fait pas**
- Ne masque pas les réponses entre balises `#- ... -#`
- Ne transforme pas les balises en champs (SDT)
- Ne nettoie pas les doublons ou variantes de style
- Ne vérifie pas l’ordre ou la validité pédagogique des blocs

Ces étapes sont réalisées par la **passe 1** et la **passe 2**.

---

## 7. Prochaines évolutions prévues (v2.05+)
- Ajout d’une **logique plus robuste** pour l’insertion automatique des balises `#Q` / `#A` basée sur des motifs textuels
- Journalisation dans un fichier `.log`
- Validation de la structure ligne par ligne (type linting)
