def bon_indent():
    print("Ligne avec indentation correcte")  # 4 espaces ici
    if True:
        print("Niveau 2 : encore 4 espaces")

def mauvais_indent():
	print("ATTENTION : cette ligne est indentée avec un tab !")  # ← devrait déclencher une ampoule
