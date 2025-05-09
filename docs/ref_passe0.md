# 🔧 Passe 0 — Génération de fichiers linéaires

## Version actuelle : v2.14

La version 2.14 introduit la standardisation des chemins, balises et fonctions partagées via le module `passe_tools.py`, utilisé par toutes les passes.

### ✅ Fonctionnalités principales
- Conversion automatique des tableaux Word en `.docx` linéaire
- Insertion de balises : `#Q#######`, `#A-------`, `#RC_...`, `@ImgSize:`, `@RefBAK:`
- Insertion réelle des images dans le document
- Préparation complète pour traitement en passe1

---

## 📘 Versions détaillées

| Version | Description                  | Détail complet                |
|---------|------------------------------|-------------------------------|
| v2.13   | Insertion images et `@ImgSize:` | [ref_passe0_2.13.md](ref_passe0_2.13.md) |
| v2.12   | Références pédagogiques `@RefBAK:` | [ref_passe0_2.12.md](ref_passe0_2.12.md) |


## 🔧 Options CLI disponibles

Le script principal `passe0_docx_tab_to_lin.py` ne prend actuellement **aucun argument en ligne de commande**.

Les options seront introduites dans une future version pour :
- traiter un seul fichier donné en argument
- activer un mode de débogage ou de validation intermédiaire