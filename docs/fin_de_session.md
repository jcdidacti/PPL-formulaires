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
