
# 📋 Mémo rapide : Comment archiver un fichier de documentation

Utilise ce script pour archiver proprement un fichier de `docs/` vers `docs/archive/` :

```bash
python scripts/archiver_fichier.py --file nom_fichier.md --prefix old_
```

- `--file` : le **nom du fichier** dans `docs/`
- `--prefix` : le **préfixe obligatoire** (ex: old_, legacy_, archive_, vYYYY-MM-DD_)

Exemple :
```bash
python scripts/archiver_fichier.py --file bloc_notes.md --prefix old_
```

✅ Le fichier sera déplacé automatiquement dans `docs/archive/` et renommé.

---

# 📦 Dossier `archive/` — Fichiers déplacés

Ce dossier contient des fichiers déplacés ou obsolètes que l’on souhaite conserver **pour référence**, sans les garder au premier plan dans `docs/`.

---

## 📁 Contenu typique :
- Versions précédentes de fichiers `.md`
- Anciennes consignes ou résumés de session
- Fichiers fusionnés avec d’autres documents plus récents

---

## 📄 Exemple déplacé :
- `nouvelle_conversation_GPT.md` → remplacé par `reprise_projet_ppl.md`

---

## 🧾 Convention de nommage recommandée

| Préfixe       | Usage                                              | Exemple                               |
|---------------|----------------------------------------------------|----------------------------------------|
| `old_`        | Version précédente simple                          | `old_workflow.md`                      |
| `legacy_`     | Ancien format non utilisé mais documenté           | `legacy_structure_2024.md`            |
| `archive_`    | Fichiers déplacés sans remplacement exact          | `archive_sujet_numerique.md`          |
| `vYYYY-MM-DD_`| Sauvegarde datée pour restauration ciblée          | `v2025-04-25_bloc_notes.md`           |

---

Garde cette convention en tête pour organiser les fichiers obsolètes sans perte d’historique. Tu peux renommer avant ou après déplacement.
