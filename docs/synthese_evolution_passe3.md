
# 🧠 Synthèse stratégique : Évolution vers Passe 3 et au-delà

Ce document sert de base de réflexion pour structurer les prochaines étapes du projet, en particulier la séparation ou intégration des passes, la génération des documents finaux, et l’organisation des questions par chapitre et questionnaire.

---

## 🧭 1. Passe 1 et Passe 2 — ensemble ou séparés ?

### 🟢 Avantages d’un script unique :
- Simplicité d’exécution pour l’auteur
- Moins de fichiers intermédiaires à gérer
- Plus fluide pour les tests itératifs

### 🔴 Inconvénients :
- Moins clair si on veut tester uniquement la syntaxe (`passe2`)
- Risque d’alourdir le script au fil des fonctions

### ✅ Recommandation :
> Créer **une fonction `verifier_txt()`** **optionnelle dans `passe1`**.  
> Elle pourra être appelée :
- automatiquement à la fin de la génération
- ou séparément par un paramètre `--check`

---

## 🧭 2. Développement parallèle de la Passe 3

### 🧩 Objectif :
> Générer deux documents `.docx` :
- **Instructeur** avec réponses visibles
- **Élève** avec champs à remplir

### 🔁 Démarche :
- Commencer par générer un document de base (`docx`) avec en-tête et une question
- Ajouter progressivement :
  - Références BAK
  - Balises de type
  - Images
  - Champs SDT (réponse élève)
  - Styles personnalisés
- Tester chaque ajout dans un cycle itératif

---

## 🧾 3. Intégration des références de cours (BAK)

- Les réponses peuvent débuter par : `BAK 3.1.2`, ou une plage `BAK 3.1.2 - 3.2`
- Cette info doit apparaître :
  - Dans le **document instructeur**
  - Dans le **document élève** pour guider la recherche
- Elle est extraite automatiquement dans `passe3` depuis la réponse

---

## 📋 4. Numérotation et groupes de questions (vision modulaire)

### 🎯 Vision :
Chaque fichier chapitre (ex. `00-2-04`) contient **un pool de questions versionnées**.

#### Catégories :
- `#Q01.1 [OBLIGATOIRE]`
- `#Q01.2 [VARIANTE:ex1]`
- `#Q01.3 [VARIANTE:ex1]`
- `#Q01.4 [VARIANTE:ex1]`

### 🔁 Pour les questionnaires :
- L’auteur définit un **sous-ensemble de questions** à inclure
- Ex : toutes les `OBLIGATOIRE` + 1 variante par groupe

### ✅ Avantages :
- Flexibilité entre les élèves
- Traçabilité des variantes utilisées
- Reproductibilité par versionnage

---

## 📂 5. Prochaine formalisation

À prévoir :

- ✅ Un fichier `.md` pour décrire :
  - Le format des questions
  - Les options possibles : `OBLIGATOIRE`, `VARIANTE:x`
  - La structure d’un fichier de sélection de questions
- ✅ Intégration dans `workflow.md` à terme

---

## 🔄 Démarche de développement recommandée

1. **Réflexion & modélisation** (.md)
2. **Prototype technique minimal (1 cas)**
3. **Test sur un chapitre complet**
4. **Intégration dans un script stable**
5. **Documentation officielle du format**

---

Tu peux annoter, compléter ou amender ce document à tout moment dans `docs/`.
