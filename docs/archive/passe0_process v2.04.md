
# Processus de la passe 0 — Conversion des fichiers .docx avec tableaux en fichiers linéaires

Ce document résume le fonctionnement du script `passe0_docx_tab_to_lin_img.py` (version 2.04), utilisé pour transformer des fichiers `.docx` contenant des tableaux (questions/réponses, images) en fichiers texte linéaires compatibles avec la suite du projet PPL-Formulaires.

## Étapes principales du traitement

### Étape 1. Initialisation des chemins et constantes
- Détection automatique du répertoire contenant les fichiers `.docx` source (`data/00docx_tab`).
- Création automatique des répertoires de sortie (`data/01docx_lin_in`, `log`, `images`) si nécessaires.
- Chargement de la liste des fichiers `.docx` à traiter.

### Étape 2. Extraction des images depuis les cellules
- Chaque cellule est analysée pour détecter les éventuelles images.
- Les images sont extraites et enregistrées dans un dictionnaire `images_par_cellule` avec leur nom unique.
- Ce dictionnaire est indexé par une clé (numéro de table, ligne, colonne) et un type (`Q` pour question, `R` pour réponse).

### Étape 3. Transformation du tableau en texte linéaire
- Les tableaux sont parcourus ligne par ligne.
- Pour chaque ligne :
  - Le contenu des cellules (gauche et droite) est nettoyé et assemblé.
  - La langue est détectée (`fr` si ligne commence par `Défi |`, `de` si `Herausforderung |`).
  - Les balises d’entête, de structure (`##Identification`, `##Work Start`, `##Work End`) sont insérées au bon endroit.
  - Un repère `#RC_table_row_Q` ou `#RC_table_row_R` est inséré si la cellule contient une image.
  - Si les balises `#Q#######` ou `#A-------` sont absentes mais la ligne est structurée, elles peuvent être ajoutées automatiquement (fonctionnalité à affiner dans la v2.05).

### Étape 4. Structuration des blocs Q/A
- Le contenu brut est analysé pour reformater correctement chaque bloc de question/réponse :
  - Ligne séparée pour la question avec `#Q########################################################`
  - Repère d’image associé (`#RC_...`)
  - Ligne `#A-----------------------------------------------------------------------------------` pour marquer le début de réponse
  - Repère d’image associé (`#RC_...`)
  - Texte de la réponse nettoyé

### Étape 5. Génération du document linéaire final (.docx)
- Le fichier de sortie est généré ligne par ligne avec gestion :
  - Des sauts de ligne
  - Des balises
  - Des sauts de page `[PAGEBREAK]`
  - Des styles neutres (sans mise en forme)
- Le fichier est sauvegardé dans `data/01docx_lin_in/` avec le même nom que le fichier d’origine.

## Logique de détection d’images
- Les images sont extraites **par cellule**, pas globalement.
- Chaque image est identifiée par son contenu (SHA1) pour éviter les doublons.
- Un repère `#RC_table_row_Q` ou `#RC_table_row_R` est ajouté dans le fichier texte pour lier les images à leur position d’origine.

## Particularités
- Certaines lignes sont ignorées si vides ou hors du bloc de langue actif.
- Les sections “Temps passé à ce défi” déclenchent la clôture du bloc par `##Work End`.
- L’en-tête est inséré automatiquement dès détection du début de bloc `Défi |` ou `Herausforderung |`.

## Ce que la passe 0 **ne fait pas**
- Ne masque pas les réponses entre balises `#- ... -#`.
- Ne transforme pas les balises en champs de formulaire (SDT).
- Ne restructure pas finement les styles ni les doublons.
- Ne vérifie pas la cohérence pédagogique ou grammaticale.

Ces étapes sont prises en charge par les passes suivantes (`passe1`, `passe2`).

## Prochaines améliorations (prévue pour v2.05)
- Ajout d’un module de détection automatique des balises `#Q#######` / `#A-------` basé sur la structure du contenu.
- Meilleure journalisation (fichier `.log`).
- Validation syntaxique ligne à ligne (type linting).
