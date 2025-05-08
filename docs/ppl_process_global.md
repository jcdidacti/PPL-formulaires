# 📄 ref_methodo.md

# 🧭 Méthodologie générale — PPL-Formulaires

Ce projet suit un processus structuré en passes successives pour assurer la transformation complète et contrôlée des questionnaires en formats pédagogiques utilisables, tout en assurant la compatibilité entre outils.

## 🎯 Objectif de la passe 0
Fournir un fichier `.docx` linéaire, balisé, contenant tout le nécessaire pour être traité automatiquement dans la passe 1.

## 🔁 Cycle projet recommandé

1. **Valider que la passe 1 traite correctement la sortie de la passe 0**
2. **Choisir la forme d'intégration des nouveaux questionnaires** :
   - Format tableau `.docx` (recommandé pour la rédaction initiale)
   - ou format linéaire `.docx` (recommandé pour l’évolution technique)
3. **Intégrer progressivement toutes les balises prévues dans `balises.md`**
4. **Préparer deux sorties finales** :
   - Un document instructeur (avec tout le contenu)
   - Un document élève (avec masquage, aide, etc.)
5. **Maintenir une compatibilité complète passe0 → passe1 → passe2**

## 📌 Décision actuelle
> Rédaction initiale en **tableau Word**, transformation via la **passe 0**, puis édition/évolution possible en **format linéaire**.

---

# 📄 ref_passe0.md

# 🔧 Passe 0 — Génération de fichiers linéaires

## Version actuelle : v2.13

### ✅ Fonctionnalités
- Conversion automatique des tableaux Word en `.docx` linéaire
- Insertion de balises :
  - `#Q#######`, `#A-------`
  - `#RC_T_R_Q|R`, `@ImgSize: height_cm = 4`
  - `@RefBAK:` extrait automatiquement depuis `#BAK ... BAK#`
- Insertion réelle des images dans le `.docx`, selon les repères
- Balises visibles dans le document (avec formatage)

### 📂 Fichiers produits
- Document `.docx` linéaire complet
- Log individuel + log global
- Export intermédiaire `*_av_struct_*.txt`

### 📄 Exemple de résultat

```
#Q########################################################
#RC_1_2_Q
@ImgSize: height_cm = 4
@RefBAK: BAK 40 [2.3.3 p44]

Quelle est la pression de référence...

#A-----------------------------------------------------------------------------------
#RC_1_2_R
@ImgSize: height_cm = 4

Les cônes...
```

### 🚫 Limites connues (v2.13)
- La hauteur est fixée à 4 cm (lecture dynamique de `height_cm = ...` non encore active)
- Aucune validation du contenu des balises dans cette passe
- `@ImgSize:` présent même sans image (utilisable pour contrôle ultérieur)

### 🔄 Historique
- v2.13 : intégration réelle des images + balise `@ImgSize:` affichée
- v2.12 : `@RefBAK:` injecté automatiquement
- v2.11 : structuration Q/A même sans balises
- v2.04 : repères ligne/image + journalisation

---

# 📄 ref_passe1.md

# 🔄 Passe 1 — (à définir)

> À compléter une fois que la compatibilité avec la passe0 v2.13 est validée.

---

# 📄 ref_passe2.md

# 🧪 Passe 2 — Validateur syntaxique `.txt`

> À compléter ou synchroniser avec `passe2_validator.py`.

- Vérification des balises d’identification
- Validation des blocs de langue
- Contrôle de la structure : `#Q`, `#A`, `##Introduction`, etc.

---

# 📄 ref_balises.md

# 📚 Conventions de balisage — PPL-formulaires

Ce document définit **l'ensemble des balises utilisées** dans les fichiers `.txt` du projet.  
Toutes les conventions ici décrites sont **obligatoires** et font l'objet de contrôles automatisés via le validateur `passe2_validator.py`.

---

## 1. 🔖 Balises d’en-tête (structure obligatoire lignes 1 à 5)

| Ligne | Balise            | Description                                 |
|-------|-------------------|---------------------------------------------|
| 1     | `##Identification`| Démarre un nouveau bloc de langue           |
| 2     | `#Script`         | Script ayant généré ce fichier              |
| 3     | `#Run at`         | Date/heure de génération                    |
| 4     | `#ID file`        | Nom du fichier source                       |
| 5     | `##LANG-fr`       | Langue du bloc (`fr`, `de`, etc.)          |

✅ Ces lignes doivent apparaître **dans cet ordre exact**, sans saut ni ligne vide.

---

## 2. 📝 Balises de description (lignes 6 à 9)

| Ligne | Balise     | Obligation     | Commentaire                           |
|-------|------------|----------------|----------------------------------------|
| 6     | `#ID`      | Obligatoire    | Identifiant du défi ou document       |
| 7     | `#Version` | Obligatoire    | Numéro de version                     |
| 8     | `#Date`    | Obligatoire    | Date du document (format libre)       |
| 9     | `#Author`  | Obligatoire    | Initiales de l’auteur (**même en français**) |

❌ Variantes comme `#Auteur` sont **refusées**.

---

## 3. ❓ Balises de contenu (questions / réponses)

| Balise      | Description                       |
|-------------|-----------------------------------|
| `#Q######`  | Début de question (nombre variable de `#`) |
| `#A------`  | Début de réponse (nombre variable de `-`)  |

---

## 4. ⛔ Balises de stucture

| Balise           | Rôle                                           |
| ---------------- | ---------------------------------------------  |
| `##Introduction` | Début de la section d’introduction             |
| `##Work Start`   | Début du bloc de questions                     |
| `##Work End`     | Fin du bloc de questions                       |
| `##Form End`     | Termine complètement le fichier multilingue    |



---

## 5. 🧪 Balises de champs de réponse (à masquer ou évaluer)

| Syntaxe             | Description                              |
|---------------------|------------------------------------------|
| `#- ... -#`         | Champ masqué dans la version élève       |
| `[type:mot]`        | (optionnel) Type de réponse attendue     |

**Types autorisés** :
- `type:image` → réponse sous forme de dessin
- `type:mot`   → mot-clé ou nom technique
- `type:num`   → valeur numérique
- `type:text`  → phrase ou explication

Exemple :
```
#-[type:num] 345 -#
```

---

## 6. 📌 Règles générales

- Toutes les balises doivent :
  - commencer **en début de ligne**
  - être **strictement conformes à l’orthographe attendue** (`#Author`, pas `#Auteur`)
- Le validateur ignore les blocs de langue mal commencés (sans `##Identification`)
- Les erreurs sont annotées dans les fichiers `.annotated.txt` générés automatiquement


---

## 7. 🧱 Structure logique recommandée du fichier `.txt`

Pour une reconstruction automatique fiable vers `.docx` / `.odt`, il est recommandé d'organiser chaque fichier en **blocs bien séparés** à l'aide de balises structurantes.

### ✅ Ordre des sections pour chaque langue :

```
##Identification
#Script : ...
#Run at : ...
#ID file : ...
##LANG-fr
#ID : ...
#Version : ...
#Date : ...
#Author : ...

##Introduction
[texte facultatif destiné à l’élève]

##Work start
#Q...
#A...
...

##Work end

##LANG-de
(même structure que ci-dessus pour l’allemand)

#Form end
```

---

### ✳️ Balises supplémentaires proposées

| Balise | Rôle |
| ------ | ---- |
|        |      |
|        |      |
| `      |      |
|        |      |
|        |      |

---

💬 **Remarques :**

- Toute balise ajoutée doit être **unique** dans le bloc de langue et toujours **placée seule en début de ligne**.

---

Tu peux proposer d'autres balises via les tests ou au fil du développement. Ce fichier sera mis à jour régulièrement.


---

## 8. 🎯 Balises avancées pour individualisation, sélection et sécurité

Ces balises sont destinées à enrichir les questionnaires pour :
- identifier les questions obligatoires vs facultatives,
- proposer des variantes individuelles,
- structurer par thème de cours,
- et ajouter un mécanisme d'authentification.

### 8.1 🔐 Statut de la question

À ajouter juste **après  une balise `#Q`**, dans une ligne séparée :

```
@MandatoryQ   (cette directive rend la question obligatoire. C'est le cas par défaut)
@OptionalQ    
```

💬 Par défaut, toute question est considérée comme obligatoire si aucune directive n’est précisée.

---

### 8.2 🎲 Groupe de variantes (tirage aléatoire)

Pour indiquer que plusieurs questions sont des variantes mutuellement exclusives (A, B, C…), on ajoute :

```
@Group:A-1
@Group:A-2
@Group:A-3
```

Les générateurs peuvent alors tirer **une seule question par groupe** pour un élève donné. 
Dans l'exemple ci-dessous on voit 3 questions pour le groupe A

💬 Les groupes ne doivent pas se superposer. Une question appartient à **au plus un groupe**.

---

### 8.3 🧭 Thème ou objectif pédagogique

Chaque question peut être reliée à un **objectif ou section de cours** :

```
@Theme:BAK 3.2.4
@Theme:Analyse graphique
```

Le descriptif du thème est libre, mais les questions d'un même thème doivent avoir le même texte.

Cela permet de garantir que le test final couvre **un pourcentage représentatif** de la matière (ex. 75%).

---

### 8.4 🔒 Code d'authentification personnel

Le haut du document (dans `##Identification`) peut contenir une ligne :

```
#Code : <à compléter par l’élève>
```

Le système peut vérifier ce champ ou le croiser avec un identifiant individuel.

---


### 8.5 🗒️ Texte explicite de la question

Afin de séparer clairement les métadonnées (comme `@Theme` ou `@Group`) du **texte réel de la question**, on peut utiliser la balise :

```
@TextQ:
```

Elle marque le **début explicite du contenu affiché à l'élève**.

💬 Cela permet de sécuriser l’interprétation et de garantir que le texte suivant ne sera pas confondu avec une autre balise.

Exemple :

```
#Q#####
@MandatoryQ
@Group:B-1
@Theme:BAK 2.1.3
@TextQ:
Quelle est la fonction de l’altimètre ?
#A-----
#-[type:text] #-Indiquer l’altitude par rapport à un isobare de référence-#
```


### 💡 Exemple combiné

```
#Q#####
@MandatoryQ
@Group:B-1
@Theme:BAK 2.1.3 Quelle est la fonction de l’altimètre ?
#A-----
#-[type:text] #-Indiquer l’altitude par rapport à un isobare de référence-#
```

---

Ces balises avancées seront intégrées progressivement aux outils de validation et de génération automatique.

---

