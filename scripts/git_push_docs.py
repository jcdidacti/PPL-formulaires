import subprocess

print("=== 🔁 PPL-Formulaires : Synchronisation Git ===\n")

# Étape 1 : ajouter tous les fichiers modifiés
subprocess.run(["git", "add", "."], check=True)

# Étape 2 : demander un message de commit
message = input("📝 Message de commit : ").strip()
if not message:
    message = "🔄 Mise à jour documentation PPL-formulaires"

# Étape 3 : commit
subprocess.run(["git", "commit", "-m", message], check=True)

# Étape 4 : push
subprocess.run(["git", "push"], check=True)

print("\n✅ Modifications poussées avec succès !")