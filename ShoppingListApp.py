shopping_list = []

def show_menu():
    print("\n--- Menu de la liste de course ---")
    print("1. Afficher la liste de course")
    print("2. Ajouter un article")
    print("3. Supprimer un article")
    print("4. Effacer la liste de course")
    print("5. Sauvegarder la liste de course")
    print("6. Charger la liste de course")
    print("7. Quitter")

while True:
    show_menu()
    choice = int(input("Votre choix (1-7): "))

    if choice == 1:
        print("\n--- Liste de course ---")
        if not shopping_list:
            print("La liste de course est vide.")
        else:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
    elif choice == 2:
        item = input("Entrez l'article a ajouter: ")
        shopping_list.append(item)
        print(f"{item} a bien été ajoutee a la liste de course.")
    elif choice == 3:
        item = input("Entrez l'article a supprimer: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} a bien été supprime de la liste de course.")
        else:
            print(f"{item} n'est pas dans la liste de course.")
    elif choice == 4:
        shopping_list.clear()
        print("La liste de course a bien été effacee.")
    elif choice == 5:
        with open("shopping_list.txt", "w") as file:
            file.write("\n".join(shopping_list))
        print("La liste de course a bien été sauvegardee.")
    elif choice == 6:
        try:
            with open("shopping_list.txt", "r") as file:
                shopping_list = file.read().splitlines()
            print("La liste de course a bien été chargée.")
        except FileNotFoundError:
            print("Le fichier de sauvegarde n'existe pas.")
    elif choice == 7:
        print("\n--- A bientôt !!! ---")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")