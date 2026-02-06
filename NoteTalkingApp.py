from datetime import datetime


FILE_NAME = "mesNotes.txt"

def show_menu():
    print("\n--- Menu de notes ---")
    print("1. Ajouter une note")
    print("2. Afficher les notes")
    print("3. Supprimer une note")
    print("4. Quitter")

def add_note():
    maintenant = datetime.now()
    heure_actuelle = maintenant.strftime("%H:%M:%S")
    date_actuelle = maintenant.strftime("%d/%m/%Y")
    note = input("Entrez votre note : ")
    with open(FILE_NAME, "a") as file:
        file.write(f"\n[{heure_actuelle} - {date_actuelle}]: {note}\n")
    print("Note ajoutée avec succès.")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("\n--- Notes ---")
                print(content)
            else:
                print("Aucune note enregistrée.")
    except FileNotFoundError:
        print("Le fichier de notes n'a pas encore été créé.")

def delete_note():
    confirm = input("Etes-vous sur de vouloir supprimer cette note ? (O/n) : ")
    if confirm.lower() == "o":
        with open(FILE_NAME, "w") as file:
            pass
        print("Note supprimée avec succès.")
    else:
        print("Suppression annulée.")


while True:
    show_menu()
    choice = input("Votre choix (1-4): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Merci d'avoir utilisé Note Talking App !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")