ingredients_recette = {"Farine", "Sucre", "Beurre", "Oeufs", "Lait"}

user_input = input("Entrez les ingrédients que vous avez (séparer par des virgules : )")

user_ingredients = set(user_input.split(","))

ingredients_manquants = ingredients_recette - user_ingredients

ingredients_supplementaires = user_ingredients - ingredients_recette

print("\n--- Check des ingrédients ---")

if ingredients_manquants:
    print(f"Ingrédients manquants : {', '.join(ingredients_manquants)}")
else:
    print("Vous avez tous les ingrédients necessaires.")