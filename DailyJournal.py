import datetime

JOURNAL_FILE = "journal.txt"

def add_entry():
    now = datetime.datetime.now()
    heure_actuelle = now.strftime("%H:%M:%S")
    date_actuelle = now.strftime("%d/%m/%Y")
    entry = input("Ecrivez dans votre journal : ")
    with open(JOURNAL_FILE, "a") as file:
        file.write(f"[{heure_actuelle} - {date_actuelle}]: {entry}\n")
    print("Entree ajouté avec succès.")

def view_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.read()
            if content:
                print("\n--- Journal ---")
                print(content)
            else:
                print("Aucune entree enregistrée. Commencez a ecrire aujourd'hui ! :D")
    except FileNotFoundError:
        print("Le fichier de journal n'a pas encore été cree.")

def search_entries():
    keyword = input("Entrez la mot cle de recherche : ").lower()
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()
            found = False
            print("\n--- Resultats de recherche ---")
            for entry in entries:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("Aucune entree trouvee correspondant a votre mot cle.")
    except FileNotFoundError:
        print("Le fichier de journal n'a pas encore ete cree.")

def delete_entry():
    keyword = input("Entrez la mot cle de l'entree a supprimer : ").lower()
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()
        with open(JOURNAL_FILE, "w") as file:
            for entry in entries:
                if keyword not in entry.lower():
                    file.write(entry)
        print("Entree supprimée avec succès.")
    except FileNotFoundError:
        print("Le fichier de journal n'a pas encore ete cree.")


def show_menu():
    print("\n--- Menu du Journal ---")
    print("1. Ajouter une entree")
    print("2. Afficher le journal")
    print("3. Rechercher une entree")
    print("4. Supprimer une entree")
    print("5. Quitter")


while True:
    show_menu()
    choice = input("Votre choix (1-5): ").strip()

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        delete_entry()
    elif choice == "5":
        print("Merci d'avoir utilisé le Journal !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide (1-4).")