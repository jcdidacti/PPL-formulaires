import subprocess

def lister_tags_par_script(script_name_part):
    print(f"🔍 Tags associés à : {script_name_part}\n")
    try:
        result = subprocess.run(
            ["git", "tag", "--list", f"{script_name_part}-v*"],
            capture_output=True, text=True, check=True
        )
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("❌ Aucun tag trouvé pour ce préfixe.")
    except subprocess.CalledProcessError as e:
        print("Erreur :", e)

if __name__ == "__main__":
    print("Usage : python list_versions.py <prefixe_script>")
    print("Exemples : passe0, passe1")
    import sys
    if len(sys.argv) >= 2:
        lister_tags_par_script(sys.argv[1])
    else:
        print("\nVeuillez indiquer un nom de script comme argument.")
