# 🔧 Passe 0 — Détails version v2.14

## ✅ Objectif de cette version
- Centralisation des chemins et conventions dans `passe_tools.py`
- Génération complète de l'en-tête (##Identification) incluant :
  - #Script, #Run at, #ID file, ##LANG-xx, #ID, #Version, #Date, #Author
- Insertion automatique du bloc d’introduction par langue
- Insertion des images depuis les cellules du tableau (avec repère #RC_T_R_Q/R)
- Ajout systématique de la balise `@ImgSize: height_cm = 4` si une image est présente
- Gestion avancée des logs :
  - un log `.log` par fichier
  - un log global `log_global_passe0_v2.14.log`
  - niveaux de statut : OK / WARNING / ERROR
- Factorisation :
  - Fonction `formater_paragraphe(p)`
  - Fonction `ajouter_ligne(doc, ligne)`

## 📄 Fichier principal
- `passe0_docx_tab_to_lin.py` (structure stable renommée depuis `_v2_16_util.py`)

## 🧪 Exemple de structure générée
```text
##Identification
#Script : v2.14.py
#Run at : 2025-05-08 22:17
#ID file : 40-2-04-défi-fd.docx
##LANG-fr
#ID : 40-2-04
#Version : 1.01
#Date : 01.05.2025
#Author : BW

##Introduction

[Texte inséré automatiquement]

##Work Start
```

## 🧩 Répertoires utilisés (via passe_tools.py)
- Entrée : `data/00docx_tab/`
- Sortie : `data/01docx_lin_in/`
- Images : `data/01docx_lin_in/images/`
- Logs : `data/01docx_lin_in/log/`

## 📝 Fonctionnalités clés
- Peut traiter plusieurs langues par document
- Tolère introduction vide (avec warning), mais pas son absence (error)
- Comptabilise automatiquement questions et images