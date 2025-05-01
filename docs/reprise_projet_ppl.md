
# 🧠 Reprise du projet – Nouvelle conversation GPT (PPL-formulaires)

Ce document est à utiliser en début de **nouvelle session GPT** pour restaurer immédiatement le contexte du projet PPL-formulaires.

---

## 📘 Contexte général

- Projet : **PPL-formulaires**
- Objectif :
  - Convertir des fichiers `.docx` linéaires en questionnaires structurés
  - Générer des versions instructeur / élève
  - Mettre en place une évaluation automatique
- Organisation en passes :
  - `passe0` : tableau `.docx` → linéaire `.docx`
  - `passe1` : linéaire `.docx` → `.txt` structuré
  - `passe2` : validation et diagnostics du `.txt`
  - `passe3` : génération des `.docx` finaux
  - `passe4/5` (à venir) : évaluation des réponses

---

## 🧩 Structure du projet

- 📂 `data/` : fichiers sources et résultats intermédiaires
- 📁 `scripts/` : tous les scripts Python
- 📄 `docs/` : documentation de travail (workflow, blocs-notes, plans, modèles)

---

## ✅ Derniers fichiers de référence

| Type            | Nom                           | Rôle                           |
|------------------|-------------------------------|--------------------------------|
| Script           | `passe1_docx_lin_to_txt.py`   | Conversion `.docx` → `.txt`    |
| Documentation    | `workflow.md`                 | Structure complète du projet   |
| Documentation    | `plan_passe2_3.md`            | Plan synchronisé passe2/passe3 |
| Modèle illustré  | `modeletapes.md`              | Exemple source → instructeur/élève |
| Bloc-notes       | `bloc_notes.md`               | Idées, variantes, commentaires |

---

## 🔁 Reprise en nouvelle session GPT

> 👋 Reprise du projet **PPL-formulaires**  
> Nous travaillons désormais en parallèle sur `passe2` (validation `.txt`) et `passe3` (génération `.docx`)  
> Je vais t’envoyer les fichiers nécessaires : `.txt`, `.py`, `.md`  
> Tu retrouveras tout ce qu’il faut dans la mémoire précédente (structure, règles, conventions)

---

✅ Ce document peut être conservé dans `docs/` et copié/collé pour tout nouveau départ de session GPT.
