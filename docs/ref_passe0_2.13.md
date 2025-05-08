# 🔧 Passe 0 — Détails version v2.13

## ✅ Objectif de cette version
- Intégrer les images extraites depuis les cellules du tableau
- Insérer les images dans le `.docx` linéaire généré, à l’endroit correspondant aux repères `#RC_...`
- Ajouter systématiquement une balise `@ImgSize: height_cm = 4` après chaque repère
- Afficher visuellement cette balise dans le `.docx` (en italique gris)
- Préparer la base pour une lecture dynamique ultérieure de la hauteur (non encore active)

## 🧠 Points clés du traitement
- Les images sont extraites depuis les cellules (via `w:drawing`) et sauvegardées dans `/images`
- Les repères `#RC_T_R_Q` et `#RC_T_R_R` sont utilisés comme clés
- Lors du rendu, chaque ligne `@ImgSize:` déclenche une tentative d’insertion d’image si la clé correspondante est connue
- Si aucune image n’est trouvée : la balise est quand même insérée (prévisible et stable)

## 🧪 Exemple dans le `.docx`
```
#Q########################################################
#RC_1_2_Q
@ImgSize: height_cm = 4
@RefBAK: BAK 40 [2.3.3 p44]

Question ici...

#A-----------------------------------------------------------------------------------
#RC_1_2_R
@ImgSize: height_cm = 4

Réponse ici...
```

## 🔁 Limites
- La hauteur est fixe : `4 cm`
- Pas de validation du contenu de la balise `@ImgSize:` pour l’instant
- Toutes les images sont insérées si elles existent, aucune compression automatique

## 📄 Fichiers impliqués
- `passe0_docx_tab_to_lin_img_v2_13.py`
- `ref_balises.md`
