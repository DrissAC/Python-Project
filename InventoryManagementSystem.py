import sys
import csv
import os

sys.stdout.reconfigure(encoding='utf-8')

Inventory_file = "Inventory.csv"

class Inventory:
    total_items = 0

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity

    def show_product_details(self):
        print("\n--- Details du produit ---")
        print(f"{self.quantity} {self.product_name}(s) à {self.price}€")
    
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"Vente de {amount} {self.product_name}(s).")
        else:
            print("Quantité insuffisante.")
        if self.quantity <= 3:
            print(f"ATTENTION !!! Il reste seulement {self.quantity} {self.product_name}(s) dans l'inventaire.")

    @staticmethod
    def calculate_discount(price, discount_percentage):
        discounted_price = price * (1 - discount_percentage / 100)
        return discounted_price
    
    @classmethod
    def total_items_report(cls):
        print(f"Nombre total de produits : {cls.total_items}")

products = []

def save_to_csv():
    with open(Inventory_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nom du produit", "Prix", "Quantité"])
        for p in products:
            writer.writerow([p.product_name, p.price, p.quantity])

def load_from_csv():
    if os.path.exists(Inventory_file):
        with open(Inventory_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Inventory(row['Nom du produit'], float(row['Prix']), int(row['Quantité']))
                products.append(product)

load_from_csv()

def add_product():
    product_name = input("Nom du produit: ")
    price = float(input("Prix: "))
    quantity = int(input("Quantité: "))
    product = Inventory(product_name, price, quantity)
    products.append(product)
    save_to_csv()
    print(f"{quantity} {product_name}(s) ajouté(s) au stock.")

def view_products():
    print("\n--- Inventaire ---")
    if not products:
        print("Pas de produits dans l'inventaire.")
    else:
        for product in products:
            product.show_product_details()

def sell_product():
    product_name = input("Nom du produit a vendre: ")
    for product in products:
        if product.product_name == product_name:
            amount = int(input("Quantité a vendre: "))
            product.sell_product(amount)
            save_to_csv()
            break
    else:
        print("Produit non trouvé dans l'inventaire.")

def calculate_discount():
    price = float(input("Entrer le prix du produit: "))
    discount_percentage = float(input("Entrer le pourcentage de remise: "))
    discounted_price = Inventory.calculate_discount(price, discount_percentage)
    print(f"Prix avec remise: {discounted_price}€")

while True:
    print("\n--- Systeme de gestion de l'inventaire ---")
    print("1. Ajouter un produit")
    print("2. Afficher l'inventaire")
    print("3. Vendre un produit")
    print("4. Calculer le prix avec remise")
    print("5. Nombre de produits dans l'inventaire")
    print("6. Quitter")

    choice = input("Entrez votre choix (1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        sell_product()
    elif choice == "4":
        calculate_discount()
    elif choice == "5":
        Inventory.total_items_report()
    elif choice == "6":
        print("Merci d'avoir utilisé le Systeme de gestion de l'inventaire !")
        break
    else:
        print("Choix incorrect. Veuillez choisir une option valide (1-6).")