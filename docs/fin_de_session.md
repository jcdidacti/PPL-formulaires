# 📋 Guide de fin de session – Projet PPL-formulaires

## ✅ Étapes recommandées pour clore proprement une session :

1. ✅ Tester les scripts modifiés et s’assurer qu’ils fonctionnent
2. ✅ Versionner les fichiers modifiés :
   ```bash
   git add <fichiers>
   git commit -m "Message clair"
   git tag <script>-vX.XX
   git push
   git push origin <tag>
   ```
3. ✅ Mettre à jour :
   - `.gitignore` si des nouveaux chemins doivent être ignorés
   - `structure_projet.md` si la structure a évolué
   - `session_log.md` pour noter les étapes importantes de la session
4. ✅ Sauvegarde manuelle ou automatisée des fichiers (ex. via OneDrive ou script .bat)
5. ✅ (Facultatif) Créer un tag général de session :
   ```bash
   git tag session-AAAA-MM-JJ
   git push origin session-AAAA-MM-JJ
   ```

---

🧠 Objectif : reprendre facilement la prochaine fois, avec un projet propre, versionné et traçable.


---

## 🔁 En cas d'ouverture d'une nouvelle conversation GPT :

Pensez à utiliser le fichier suivant pour restaurer rapidement le contexte :

📄 `docs/nouvelle_conversation_GPT.md`

Copiez-collez son contenu en début de chat pour éviter toute perte de repères (structure, scripts, versions, etc.).

---

## 💾 Sauvegarde automatique vers OneDrive

En fin de session, exécuter le fichier :

📁 `sauvegarde_ppl_vers_onedrive.bat`

Ce script :
- Copie **l'ensemble du dossier `C:\Dev\PPL-formulaires`**
- Y compris les fichiers de **`data/`**
- Crée un dossier horodaté dans `C:\Users\jacqu\OneDrive\90 dev\sauvegardes_PPL\YYYY-MM-DD_HH-MM`

Cela permet de conserver une **trace complète** du projet à chaque fin de session.
