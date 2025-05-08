# 🧭 Méthodologie générale — PPL-Formulaires

Ce projet suit un processus structuré en passes successives pour assurer la transformation complète et contrôlée des questionnaires en formats pédagogiques utilisables, tout en assurant la compatibilité entre outils.

## 🎯 Objectif de la passe 0
Fournir un fichier `.docx` linéaire, balisé, contenant tout le nécessaire pour être traité automatiquement dans la passe 1.

## 🔁 Cycle projet recommandé

1. **Valider que la passe 1 traite correctement la sortie de la passe 0**
2. **Choisir la forme d'intégration des nouveaux questionnaires** :
   - Format tableau `.docx` (recommandé pour la rédaction initiale)
   - ou format linéaire `.docx` (recommandé pour l’évolution technique)
3. **Intégrer progressivement toutes les balises prévues dans `balises.md`**
4. **Préparer deux sorties finales** :
   - Un document instructeur (avec tout le contenu)
   - Un document élève (avec masquage, aide, etc.)
5. **Maintenir une compatibilité complète passe0 → passe1 → passe2**

## 📌 Décision actuelle
> Rédaction initiale en **tableau Word**, transformation via la **passe 0**, puis édition/évolution possible en **format linéaire**.


## 🧱 Modularisation active

Depuis la version `passe0-v2.14`, les chemins d’accès, structures d’en-tête, conventions de base et fonctions partagées sont regroupés dans un module unique `passe_tools.py`.

Ce module est désormais la référence commune pour toutes les passes, garantissant :
- une cohérence des chemins et structures
- un point de maintenance unique
- un comportement identique entre les étapes