contacts = {}

def show_menu():
    print("\n--- Menu de contact ---")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Rechercher un contact")
    print("4. Modifier un contact")
    print("5. Supprimer un contact")
    print("6. Quitter")

def add_contact():
    name = input("Nom : ")
    phone = input("Numéro de téléphone : ")
    email = input("Email : ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"{name} ajouté(e) avec succès !")

def view_contacts():
    if contacts:
        print("\n--- Liste des contacts ---")
        for name, details in contacts.items():
            print(f"Nom : {name}")
            print(f"Téléphone : {details['phone']}")
            print(f"Email : {details['email']}")
            print("------------------------")
    else:
        print("Aucun contact enregistré.")

def search_contact():
    name = input("Nom du contact à rechercher : ")
    if name in contacts:
        print(f"Nom : {name}")
        print(f"Téléphone : {contacts[name]['phone']}")
        print(f"Email : {contacts[name]['email']}")
    else:
        print(f"{name} non trouvé.")

def modify_contact():
    name = input("Nom du contact à modifier : ")
    if name in contacts:
        phone = input("Nouveau numéro de téléphone : ")
        email = input("Nouvel email : ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"{name} modifié(e) avec succès !")
    else:
        print(f"{name} non trouvé.")

def delete_contact():
    name = input("Nom du contact à supprimer : ")
    if name in contacts:
        del contacts[name]
        print(f"{name} supprimé(e) avec succès !")
    else:
        print(f"{name} non trouvé.")

while True:
    show_menu()
    choice = input("Votre choix (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        modify_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide (1-6).")