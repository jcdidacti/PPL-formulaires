# 📘 Consignes Git pour versionner les scripts PPL-formulaires

## Convention de nommage

- Les scripts ont un **nom fixe** une fois stables :
  - `passe0_docx_tab_to_lin.py`
  - `passe1_docx_lin_to_txt.py`

- Les versions sont tracées via des **tags Git** :
  - `passe0-v1.02`, `passe0-v1.03`, etc.
  - `passe1-v2.63`, `passe1-v2.64`, etc.

---

## Workflow recommandé

### Geler une version stable

```bash
git add scripts/passe0_docx_tab_to_lin.py
git commit -m "Nouvelle version passe0"
git tag passe0-v1.03
git push
git push origin passe0-v1.03
```

### Revenir à une version spécifique

```bash
git checkout passe0-v1.02 -- scripts/passe0_docx_tab_to_lin.py
```

---

## Voir l'historique des versions d'un script

```bash
python scripts/list_versions.py passe0
```

## Autres commandes utiles

```bash
git tag --list           # voir tous les tags
git show passe0-v1.03    # voir le contenu exact d’un tag
git log -- scripts/passe0_docx_tab_to_lin.py  # historique complet
```
