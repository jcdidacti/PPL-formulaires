# 🧭 Roadmap de la passe 1 — `passe1_docx_lin_to_txt.py`

Ce fichier résume les étapes techniques restantes pour finaliser la transformation multilingue structurée d’un document `.docx` linéaire vers un fichier `.txt`.

---

## ✅ Objectif global de `passe1`
Transformer un fichier `.docx` linéaire :
- en un fichier texte structuré
- avec extraction d’images
- en gérant plusieurs langues grâce à des balises `##LANG-fr`, `##LANG-de`, etc.

---

## 🧩 Étapes restantes (priorisées)

### ✅ 1. Gestion multilingue via `##LANG-xx`
- Bascule dynamique de langue selon les balises `##LANG-xx`
- Réinitialisation du compteur d’image par langue
- Avertissement si une langue est attendue mais absente
- Option : fallback vers détection implicite si balise manquante

---

### 🔜 2. Structuration des blocs par langue
Pour chaque langue détectée :
```python
bloc = header + process_blocs(blocs_langue) + footer
```
Ordre final : `fr`, puis `de`, puis `it` si présents.

---

### 🔜 3. Gestion des images
- Insertion des balises `#PICTxxx# [image: nom.png]`
- Section `## Images` à la fin du fichier `.txt`
- Références images correctement alignées avec les blocs concernés

---

### 🧪 4. Cas de test à couvrir
- ✔️ Fichier sans balise `##LANG-xx` → erreur ou détection implicite
- ✔️ Fichier avec une seule langue
- ⚠️ Balise absente ou mal placée → avertissement log
- ⚠️ Image manquante → `image_inconnue.png`

---

### 📦 5. Validation finale
- Ajout d’un tag Git : `passe1-v2.70`
- Sauvegarde du script dans `scripts/passe1_docx_lin_to_txt.py`
- Test fonctionnel sur 2–3 fichiers avec langue simple + multilingue

---

🔁 Ce fichier est à garder dans `/docs/` pour suivre les avancées sur la passe 1.
