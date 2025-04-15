import subprocess

def afficher_historique_git():
    print("\n🕰️ Historique des commits Git (récent → ancien)\n")
    try:
        result = subprocess.run(
            ["git", "log", "--pretty=format:%h | %ad | %s", "--date=short"],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Erreur lors de l'exécution de git log :", e)

if __name__ == "__main__":
    afficher_historique_git()
