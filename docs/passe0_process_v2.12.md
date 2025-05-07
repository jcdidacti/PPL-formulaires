# Passe 0 – Conversion Tableau Word → Fichier Linéaire avec Images et Balises

## 🌟 Nouveauté v2.12 : gestion des références BAK

### @RefBAK: ajout automatique
- Lorsqu'une référence de type `#BAK ... BAK#` est trouvée dans la question ou la réponse, une ligne supplémentaire est insérée dans le bloc #Q :
  ```
  @RefBAK: BAK XX [3.2.1 p44]
  ```
  avec `XX` extrait automatiquement du nom du fichier source (ex: `40-2-04` → `BAK 40`).

- Si plusieurs balises sont présentes : elles sont toutes reprises.

- Si aucune balise `#BAK ... BAK#` n'est présente, mais qu'une mention "BAK" est détectée, un avertissement est ajouté dans le log pour indiquer une balise oubliée.

- Si `#BAK` est présent sans fermeture `BAK#`, une erreur est levée et le bloc est ignoré.

---

## 🧠 Fonctionnement du script `passe0_docx_tab_to_lin_img.py` (version v2.12)

### ✅ Identique à v2.11 pour :
- Initialisation des répertoires
- Analyse ligne à ligne du tableau (début à ligne 2, fin ignorée)
- Détection de la langue
- Génération de l'en-tête `##Identification ... ##Work Start`
- Détection/insertion des balises `#Q#######` et `#A-------`
- Journalisation `.log` fichier par fichier + log global
- Repères images `#RC_...` et repères ligne `#LGnnn`

### ➕ Ajout v2.12 : extraction @RefBAK
- Fonction `extraire_et_inserer_refbak(...)`
- Invoquée dans chaque bloc Q/A pour analyser les textes Q et A
- Insertion **systématique** de la ligne `@RefBAK: ...` (vide si aucune trouvée)
- Forme canonique : `BAK XX [2.3.3]`, `BAK XX [2.3.3 p44]`, etc.

---

## 📄 Exemple produit dans le .docx linéaire

```
#Q########################################################
#RC_1_2_Q

@RefBAK: BAK 40 [2.3.3 p44]

1 Décrire brièvement les types de cellules visuelles

#A-----------------------------------------------------------------------------------
#RC_1_2_R

Les cônes ...
```

---

## 🚫 Limites connues (v2.12)
- Les références non balisées `BAK 3.2.1` sont ignorées (avertissement)
- Aucun traitement intelligent des suffixes ("voir page ...")
- Les balises doivent être présentes dans le Word source : `#BAK ... BAK#`

---

## 🔄 Historique
- **v2.04** : détection conditionnelle des balises Q/A
- **v2.10** : structuration par langue, détection auto, en-tête générée
- **v2.11** : log complet, erreurs structurelles, repères ligne + image
- **v2.12** : détection et insertion de `@RefBAK:` depuis les balises `#BAK ... BAK#`

---
