# 🔧 Passe 0 — Détails version v2.12

## ✅ Objectif de cette version
- Ajouter la balise `@RefBAK:` dans chaque bloc #Q si des balises `#BAK ... BAK#` sont détectées dans la question ou la réponse

## 🧠 Fonctionnement
- Recherche de toutes les paires `#BAK ... BAK#`
- Nettoyage du texte original
- Insertion d’une ligne `@RefBAK: BAK XX [2.3.3 p44]` avec le préfixe XX extrait du nom de fichier
- En cas de mention `BAK` sans balise, un warning est ajouté dans le `.log`
- En cas de balise non fermée, une erreur bloquante est générée

## 🧪 Exemple de sortie
```
#Q########################################################
#RC_1_2_Q
@RefBAK: BAK 40 [2.3.3 p44]

Question ici...

#A-----------------------------------------------------------------------------------
#RC_1_2_R

Réponse ici...
```

## 📄 Limites
- Aucun traitement des mentions `BAK ...` hors balises
- Suffixes comme `p44`, `S45` sont conservés dans le champ `[...]`
- Ne gère pas encore les hauteurs d’images ou autres balises

## 📄 Fichiers impliqués
- `passe0_docx_tab_to_lin_img_v2_12.py`
