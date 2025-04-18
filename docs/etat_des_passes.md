# 🧭 Suivi global des passes – Projet PPL-formulaires

Ce fichier permet de visualiser l’état d’avancement de chaque passe du projet.

| Passe | Objectif court                           | Script                          | Entrée                         | Sortie                         | Version taguée | Statut     |
|-------|-------------------------------------------|----------------------------------|--------------------------------|--------------------------------|----------------|------------|
| 0     | Conversion docx (tableau → linéaire)     | passe0_docx_tab_to_lin.py       | 00docx_tab/                    | 01docx_lin_in/ + log/          | passe0-v1.03   | ✅ Terminé |
| 1     | Extraction texte + images des .docx       | passe1_docx_lin_to_txt.py       | 02docx_lin_out/                | 02text_p1_out/ + log/images/   | passe1-v2.65   | ✅ Terminé |
| 2     | Reformulation en questions ouvertes       | *(à définir)*                   | 02text_p1_out/                 | 03text_p2_out/                 | *(à définir)*  | ⏳ À faire |
| 3     | Vérification syntaxique & enrichissement  | *(à définir)*                   | 03text_p2_out/                 | 04text_p3_out/                 | *(à définir)*  | ⏳ À faire |
| …     |                                           |                                  |                                |                                |                |            |

---

✅ Statut possible :
- ✅ Terminé
- ⏳ À faire
- 🚧 En cours
- ❌ Abandonné

📝 Ce fichier est à mettre à jour manuellement après chaque passe ou tag.
