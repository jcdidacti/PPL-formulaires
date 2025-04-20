# 📁 Structure du projet PPL-formulaires

## 🗂 Arborescence des dossiers `data/` (contenu des branches)

```
/data/
├── 00docx_tab/             # fichiers .docx sous forme de tableau
├── 01docx_lin_in/          # fichiers linéarisés automatiquement
│   └── log/                # logs liés à la transformation tableau → linéaire
├── 02docx_lin_out/         # version manuellement nettoyée et relue
├── 02text_p1_out/          # fichiers texte générés à partir de .docx linéaire
│   ├── images/             # images extraites (noms: identifiant + _imageXXX)
│   └── log/                # journaux de transformation
```

## 🗂 Répertoire des scripts

```
/scripts/
├── passe0_docx_tab_to_lin.py              # transformation tableau vers linéaire
├── passe1_docx_lin_to_txt_multilingue0.py # transformation linéaire vers .txt avec images
├── list_versions.py                       # affiche les versions taguées
├── compare_files.py                       # compare deux scripts ligne par ligne
```

## 📄 Répertoire `docs/` (documentation du projet)

```
/docs/
├── structure_projet.md                        # ce fichier : vue d’ensemble
├── convention_multilingue.md                  # gestion des balises ##LANG-fr, ##LANG-de, etc.
├── fin_de_session_avec_sauvegarde_test.md     # procédures de sauvegarde automatique locale
├── reprise_conversation_GPT.md                # résumé à lire pour redonner le contexte à GPT
├── git_consigne_versioning.md                 # consignes pour versionner script par script
├── suivi_scripts_etat.md                      # tableau d’état de développement des scripts
├── 99_renommer_docs_git.md                    # comment renommer les fichiers docs en conservant le suivi Git
```

## 💡 À faire pour sauvegarder toute la documentation :
Ajouter régulièrement tous les fichiers `.md` présents dans `docs/` :

```bash
git add docs/*.md
git commit -m "Mise à jour de la documentation"
git push
```
