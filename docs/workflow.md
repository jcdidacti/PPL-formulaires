
# 📘 Workflow général du projet PPL-Formulaires

Ce document décrit l’ensemble du **flux de traitement** des questionnaires, depuis les documents d’origine jusqu’aux fichiers finalisés et évalués. Il sert de **fil conducteur global** pour structurer les passes techniques, les formats de fichiers, les rôles impliqués et les améliorations à prévoir.

---

## 🧭 Vue d'ensemble (par rôle)

| Rôle                  | Tâches principales                                                                 |
|-----------------------|------------------------------------------------------------------------------------|
| **Auteur**            | Préparer les questions, intégrer les balises, maintenir le fichier `.docx`       |
| **Script (passe 0→4)**| Automatiser le traitement et la structuration                                     |
| **Élève**             | Remplir le questionnaire (format adapté)                                          |
| **Correcteur**        | Valider les réponses (automatiquement ou manuellement)                            |

---

## 🔄 Passes de traitement

### 🟨 Passe 0 — Conversion tableau → linéaire (`passe0_docx_tab_to_lin.py`)
- 📥 **Input** : fichiers `.docx` au format tableau
- 📤 **Output** : fichiers `.docx` linéaires, prêts pour enrichissement
- 🛠️ Objectif : permettre la migration des questionnaires existants
- 🔁 **Usage : une seule fois**, le tableau n’est plus utilisé ensuite

---

### 🟦 Passe 1 — Structuration linéaire (`passe1_docx_lin_to_txt.py`)
- 📥 **Input** : fichier `.docx` linéaire maintenu par l’auteur
- 📤 **Output** : fichier `.txt` structuré + images extraites + logs
- 🎯 Objectif :
  - Structuration des questions (`#Q`) / réponses (`#A`)
  - Intégration des images (`#PICTnnn#`)
  - Vérification des langues (`##LANG-fr`, `##LANG-de`, etc.)
- 🧩 Le fichier `.docx` **reste le format de référence** pour l’auteur
- 🔁 **Usage : répété**, le fichier `.docx` peut être modifié/amélioré entre chaque passe
- 💡 Possibilité d’intégrer les balises de correction directement dans Word

---

### 🟩 Passe 2 — Normalisation / vérification syntaxique (à venir)
- 📥 **Input** : fichier `.txt` produit par la passe 1
- 🎯 Objectif :
  - Vérification de la structure (noms d’image cohérents, blocs langue complets, etc.)
  - Correction des erreurs de syntaxe ou d’oubli de balises
- 🔁 Utilisable plusieurs fois à mesure que l’auteur améliore le contenu

---

### 🟦 Passe 3 — Génération des fichiers élèves/instructeurs
- 📥 **Input** : fichier `.txt` structuré
- 📤 **Output** :
  - Version `.docx` avec champs à remplir (`SDT`), verrouillée
  - Version `.odt` si besoin (LibreOffice)
  - Version `.pdf` exportable
- 🎯 Objectif : fournir un document clair et sécurisé à l’élève
- 🧩 Peut aussi inclure un export "instructeur" avec réponses visibles

---

### 🟥 Passe 4 / 5 — Correction & évaluation
- 📥 **Input** : fichier rempli par l’élève
- 📤 **Output** : note, feedback, fichier annoté
- 🔎 Correction par type :
  - `type:text` : évaluation sémantique approximative
  - `type:num` : évaluation numérique (tolérance)
  - `type:mot` : correspondance exacte ou mots-clés
  - `type:image` : non automatisable → correction humaine

---

## 📄 Balises utilisées dans les fichiers `.docx` linéaires

| Balise                  | Description                                                     |
|-------------------------|-----------------------------------------------------------------|
| `##LANG-fr`, `##LANG-de`| Démarre un bloc de langue                                      |
| `#Q##########`          | Début de question                                               |
| `#A----------`          | Début de réponse                                                |
| `#-[type:text] ... -#`  | Réponse libre (explication)                                    |
| `#-[type:mot] ... -#`   | Réponse attendue = mot ou expression clé                       |
| `#-[type:num] ... -#`   | Réponse attendue = valeur numérique                            |
| `#-[type:image] ... -#` | Réponse attendue = dessin / croquis                            |
| `#PICTnnn#`             | Image automatiquement insérée                                  |
| `#COMMENTAIRE#`         | Annotation interne non transformée                             |

---

## 💾 Format de fichier de référence

| Acteur     | Format préféré                     |
|------------|------------------------------------|
| Auteur     | `.docx` linéaire enrichi           |
| Scripts    | `.txt` structuré + images `.png`   |
| Élève      | `.docx` avec champs ou `.pdf`      |
| Correcteur | `.docx` ou résultat dans tableau   |

---

## 🧠 Remarques importantes

- Les scripts sont pensés pour **réutiliser le même `.docx` enrichi** à chaque passe.
- La **structuration** dans Word est plus naturelle pour l’auteur que le `.txt`.
- Les balises dans les réponses permettent la **correction automatique** future.
- Le système permet de produire des documents structurés à **usage humain et machine**.

---



# 📘Workflow général du projet PPL-Formulaires

Ce document décrit les grandes étapes du flux de traitement, de l’auteur à l’évaluation.



---

## 🔄 Vue d’ensemble du flux éditorial complet

Cette section résume le **flux de transformation contrôlé** tel qu’imaginé dans le projet :

```text
1. Auteur édite :           DOCX linéaire source
                            ↓ (Passe 1)
2. Génération automatique : TXT structuré standardisé
                            ↓ (Passe 2, optionnelle)
3. Vérification syntaxique : détection d’erreurs, diagnostics
                            ↓ (Passe 3)
4. Génération des livrables : DOCX instructeur + DOCX élève
```

### 📌 Principes clés :

- L’**édition se fait uniquement dans le fichier `.docx` source linéaire**
- Le `.txt` généré est **automatique, intermédiaire et non modifié à la main**
- La **passe 2** joue un rôle de **feedback** à l’auteur (mais ne modifie rien)
- La **passe 3** produit les documents finaux, à partir d’un `.txt` validé
- Ce flux permet de :
  - Travailler proprement
  - Réutiliser facilement les questions
  - Assurer une traçabilité par versionnage


---

## 🔄 Vue d’ensemble du flux éditorial complet

Cette section résume le **flux de transformation contrôlé** tel qu’imaginé dans le projet :

```text
1. Auteur édite :           DOCX linéaire source
                            ↓ (Passe 1)
2. Génération automatique : TXT structuré standardisé
                            ↓ (Passe 2, optionnelle)
3. Vérification syntaxique : détection d’erreurs, diagnostics
                            ↓ (Passe 3)
4. Génération des livrables : DOCX instructeur + DOCX élève
```

### 📌 Principes clés :

- L’**édition se fait uniquement dans le fichier `.docx` source linéaire**
- Le `.txt` généré est **automatique, intermédiaire et non modifié à la main**
- La **passe 2** joue un rôle de **feedback** à l’auteur (mais ne modifie rien)
- La **passe 3** produit les documents finaux, à partir d’un `.txt` validé
- Ce flux permet de :
  - Travailler proprement
  - Réutiliser facilement les questions
  - Assurer une traçabilité par versionnage







## ⚠️ Difficultés potentielles à anticiper

| Problème possible                             | Solution ou précaution                                                  |
|-----------------------------------------------|--------------------------------------------------------------------------|
| Erreur de langue (bloc non balisé)            | Vérification automatique en passe 1                                     |
| Oubli d’une balise `#Q`, `#A`, `-#`            | Passe 2 = nettoyage et vérification syntaxique                          |
| Mauvais formatage du `.docx` initial          | Structuration strictement linéaire, règles de style dans le modèle Word |
| Correction automatique imprécise (type:text)  | Tolérance + post-vérification manuelle                                  |
| Images mal insérées ou dupliquées             | Système de hachage d’images en place (`md5`)                            |

---

## 🌿 Politique de branche Git

En phase de conception initiale, le projet PPL-formulaires utilise **une seule branche principale** (`main`).

### Pourquoi une seule branche ?
- Le projet est en **développement individuel**
- Chaque version est bien identifiée par un **tag Git** (`passe1-v2.70`, etc.)
- Cela simplifie la gestion et la compréhension de l’historique

### Évolutions possibles plus tard :
- Utiliser une branche `dev` si plusieurs personnes interviennent
- Créer une branche `feature/nom` pour tester une idée risquée sans casser `main`

👉 Actuellement, tout se fait sur `main`, et cela suffit.

---

Ce document est un **point de référence unique** pour tous les acteurs du projet.
