# ✏️ Renommer les fichiers `.md` en restant cohérent avec Git

## 🔁 Scénario : je souhaite renommer un fichier déjà suivi par Git

### ✅ Étapes recommandées

1. Utiliser la commande suivante :

```bash
git mv docs/ancien_nom.md docs/nouveau_nom.md
git commit -m "Renommage de fichier documentation"
git push
```

2. Le suivi Git est ainsi conservé (pas de suppression + recréation)

## ❌ Ce qu'il ne faut pas faire

- Renommer manuellement dans l'explorateur sans Git → perte de suivi
- Supprimer et recréer un fichier à la main
