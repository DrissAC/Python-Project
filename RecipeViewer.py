def load_recipes(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            recipes = content.split('\n\n')
            recipt_dict = {}
        for recipe in recipes:
            lines = recipe.strip().split('\n')
            if len(lines) >= 3 :
                name = lines[0]
                ingredients = lines[1].replace("Ingredients: ", "").strip()
                instructions = lines[2].replace("Instructions: ", "").strip()
                recipt_dict[name] = {"ingredients": ingredients, "instructions": instructions}
        return recipt_dict
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return {}
    
def show_menu():
    print("\n--- Menu des recettes ---")
    print("1. Afficher la recette par nom")
    print("2. Lister toutes les recettes")
    print("3. Rechercher recette par ingrédient")
    print("4. Ajouter une nouvelle recette")
    print("5. Quitter")

def view_recipe(recipes):
    name = input("Entrez le nom de la recette : ").strip()
    if name in recipes:
        print(f"\n--- Recette {name} ---")
        print(f"Nom : {name}")
        print(f"Ingrédients : {recipes[name]['ingredients']}")
        print(f"Instructions : {recipes[name]['instructions']}")
    else:
        print("Recette non trouvée.")

def research_by_ingredients(recipes):
    ingredient = input("Entrez l'ingrédient recherché : ").strip()
    matching_recipes = [name for name in recipes if ingredient.lower() in recipes[name]['ingredients'].lower()]
    if matching_recipes:
        print(f"\n--- Recettes contenant {ingredient} ---")
        for name in matching_recipes:
            print(name)
    else:
        print("Aucune recette ne contient cet ingrédient.")

def add_recipe(recipes):
    name = input("Entrez le nom de la recette : ").strip()
    ingredients = input("Entrez les ingrédients de la recette : ").strip()
    instructions = input("Entrez les instructions de la recette : ").strip()
    recipes[name] = {"ingredients": ingredients, "instructions": instructions}
    print(f"Recette {name} ajoutée avec succès !")

recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    choice = input("Votre choix (1-5): ")

    if choice == "1":
        view_recipe(recipes)
    elif choice == "2":
        print("\n--- Toutes les recettes ---")
        for name in recipes:
            print(name)
    elif choice == "3":
        research_by_ingredients(recipes)
    elif choice == "4":
        add_recipe(recipes)
    elif choice == "5":
        print("Merci d'avoir utilisé Recipe Viewer !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide (1-3).")