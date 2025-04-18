# 📝 Renommer les fichiers de documentation sans casser Git – Projet PPL-formulaires

Ce fichier décrit deux méthodes pour renommer proprement les fichiers `.md` dans `docs/`  
tout en **conservant leur historique Git**.

---

## ✅ Méthode recommandée : depuis le terminal avec `git mv`

Exécuter les commandes suivantes dans le terminal (depuis la racine du projet) :

```bash
git mv docs/structure_projet.md docs/00_structure_projet.md
git mv docs/nouvelle_conversation_GPT.md docs/01_reprise_nouvelle_conversation.md
git mv docs/fin_de_session.md docs/02_fin_de_session.md
git mv docs/session_log.md docs/03_journal_sessions.md
git mv docs/etat_des_passes.md docs/04_etat_des_passes.md
git mv docs/demarrage_nouvelle_passe.md docs/05_modele_nouvelle_passe.md
```

Puis valider avec :

```bash
git commit -m "Réorganisation des fichiers docs par ordre chronologique"
git push
```

---

## 🛠️ Méthode alternative : script `.bat`

Créer un fichier texte nommé `renommer_docs.bat` contenant :

```bat
@echo off
cd /d C:\Dev\PPL-formulaires
git mv docs\structure_projet.md docs\00_structure_projet.md
git mv docs\nouvelle_conversation_GPT.md docs\01_reprise_nouvelle_conversation.md
git mv docs\fin_de_session.md docs\02_fin_de_session.md
git mv docs\session_log.md docs\03_journal_sessions.md
git mv docs\etat_des_passes.md docs\04_etat_des_passes.md
git mv docs\demarrage_nouvelle_passe.md docs\05_modele_nouvelle_passe.md
git commit -m "Réorganisation des fichiers docs par script .bat"
git push
pause
```

📦 Lancer ce fichier `.bat` effectue toutes les opérations en un seul clic.

---

🧠 Quel que soit le choix, **Git conserve l'historique** des fichiers renommés.
