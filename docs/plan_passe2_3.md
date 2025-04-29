
# 🧭 Plan de travail : Développement synchronisé des passes 2 & 3

Ce fichier décrit le découpage progressif du développement des passes 2 (diagnostic/validation) et 3 (génération de documents) de manière coordonnée.

---

## 🔷 Passe 2 – Diagnostic et validation

| Étape | Objectif                                         | Priorité | Liée à…    |
|-------|--------------------------------------------------|----------|------------|
| 2.1   | Vérifier que chaque `#Q` est suivi d’un `#A`     | 🟢 Haute | 3.1, 3.2   |
| 2.2   | Vérifier la présence d’une balise `type:`        | 🟢 Haute | 3.3        |
| 2.3   | Compter les questions / réponses par langue      | 🟡 Moy   | global     |
| 2.4   | Vérifier la présence de références BAK           | 🟡 Moy   | 3.4        |
| 2.5   | Signaler les images manquantes (`#PICT`)         | 🔴 Crit. | 3.5        |
| 2.6   | Détecter les `VARIANTE:` sans groupe valide      | 🔵 Option| 3.6        |
| 2.7   | Générer un log structuré (.md ou .log)           | 🟢 Haute | retour doc |

---

## 🔶 Passe 3 – Génération de documents

| Étape | Objectif                                             | Priorité | Dépend de… |
|-------|------------------------------------------------------|----------|------------|
| 3.1   | Lire en-tête + extraire métadonnées                  | 🟢 Haute |            |
| 3.2   | Extraire Q/R propres par langue                      | 🟢 Haute | 2.1        |
| 3.3   | Afficher type de réponse et adapter le format        | 🟢 Haute | 2.2        |
| 3.4   | Insérer référence BAK dans le rendu                  | 🟡 Moy   | 2.4        |
| 3.5   | Insérer image `#PICTnnn#` avec taille personnalisée  | 🔴 Crit. | 2.5        |
| 3.6   | Affichage conditionnel selon `VARIANTE:` ou `OBLIG` | 🔵 Option| 2.6        |
| 3.7   | Générer DOCX instructeur + élève                     | 🟢 Haute | toutes     |

---

## 🧩 Stratégie recommandée

1. **Commencer par étapes 2.1, 2.2 et 3.1, 3.2, 3.3**  
   → permet de tester des Q/R types très tôt

2. **Ajouter les images et références dans 2.5 et 3.4, 3.5**

3. **Ensuite tester la sélection de variantes (2.6 + 3.6)**

4. **Valider les sorties et structure (3.7) avec différents cas**

---

Tu peux cocher chaque étape une fois validée ou testée, et l'adapter à mesure que le projet évolue.
