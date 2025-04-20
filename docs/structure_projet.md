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
├── passe1_docx_lin_to_txt.py              # version officielle actuelle avec images et balises
├── compare_files.py                       # compare deux fichiers Python
├── list_versions.py                       # affiche les tags Git par script
```

## 📄 Répertoire `docs/` (documentation du projet)

```
/docs/
├── structure_projet.md                        # ce fichier : vue d’ensemble du projet
├── convention_multilingue.md                  # gestion des balises ##LANG-fr, ##LANG-de, etc.
├── fin_de_session_avec_sauvegarde_test.md     # procédure de sauvegarde automatique des fichiers
├── reprise_conversation_GPT.md                # rappel du contexte pour réactiver GPT efficacement
├── git_consigne_versioning.md                 # consignes pour taguer proprement chaque script
├── suivi_scripts_etat.md                      # état d'avancement des scripts
├── 99_renommer_docs_git.md                    # comment renommer proprement un fichier suivi par Git
├── README.md                                  # présentation du projet et de ses objectifs
```

## 💡 Sauvegarde de la documentation
Commande à exécuter pour versionner tous les fichiers .md :

```bash
git add docs/*.md
git commit -m "Mise à jour de la documentation"
git push
```
