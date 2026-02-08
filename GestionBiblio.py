from datetime import datetime, timedelta
import json
import os

LIBRARY_FILE =  "library.json"

if not os.path.exists(LIBRARY_FILE):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump([], file)

def load_info():
    with open(LIBRARY_FILE, 'r') as file:
        return json.load(file)
    
def save_info(info):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(info, file, indent=2)


class Book:
    def __init__(self, title, author, due_date=None):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = due_date
    
    def display_info(self):
        status ="Disponible" if not self.is_borrowed else "Emprunté"
        print(f"Titre: {self.title}")
        print(f"Auteur: {self.author}")
        print(f"Statut: {status}\n")
        if self.is_borrowed and self.due_date:
            print(f"A rendre le : {self.due_date}\n")
        print("-" * 10)
    
    def generate_return_date(self):
        date_obj = datetime.now() + timedelta(days=14)
        return date_obj.strftime("%d %B %Y")




class Library:
    def __init__(self):
        self.books = []
        self.load_from_json()

    def load_from_json(self):
        data = load_info()
        self.books = []
        for item in data:
            new_book = Book(item["Livre"], item["Auteur"], item.get("date_retour"))
            new_book.is_borrowed = item["statuts"] == "Emprunte"
            self.books.append(new_book)

    def sync_database(self):
        data_to_save = []
        for b in self.books:
            status_txt = "Emprunte" if not b.is_borrowed else "Non emprunte"
            data_to_save.append({"Livre": b.title, "Auteur": b.author, "statuts": status_txt, "date_retour": b.due_date})
        save_info(data_to_save)
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        self.sync_database()
        print(f"\nLe livre {title} de {author} a bien ete ajouté.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"\nLe livre {title} est present dans notre catalogue.")
                return book
        return None

    def view_books(self):
        if not self.books:
            print("\nLa bibliothèque est vide.")
        else:
            print("\n--- Catalogue de livres ---")
            for book in self.books:
                book.display_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                book.due_date = book.generate_return_date()
                self.sync_database()
                print(f"\nLe livre {title} a bien ete emprunté. Bonne lecture !")
                print(f"\nVous avez jusqu'au {book.due_date} pour le rendre.")
                return
        print(f"\nLe livre {title} n'est pas disponible.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                book.due_date = None
                self.sync_database()
                print(f"\nLe livre {title} a bien ete rendu.")
                return
        print(f"\nLe livre {title} n'a pas encore ete emprunté.")

library = Library()

while True:
    print("\n--- Menu ---")
    print("1. Ajouter un livre")
    print("2. Afficher le catalogue")
    print("3. Rechercher un livre")
    print("4. Emprunter un livre")
    print("5. Rendre un livre")
    print("6. Quitter")

    choice = input("Entrez votre choix (1-6): ").strip()

    if choice == "1":
        title = input("Entrez le titre du livre: ").strip()
        author = input("Entrez l'auteur du livre: ").strip()
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Entrez le titre du livre que vous voulez rechercher: ").strip()
        library.search_book(title)
    elif choice == "4":
        title = input("Entrez le titre du livre que vous voulez emprunter: ").strip()
        library.borrow_book(title)
    elif choice == "5":
        title = input("Entrez le titre du livre que vous voulez rendre: ").strip()
        library.return_book(title)
    elif choice == "6":
        print("Merci d'avoir utilisé la Bibliothèque !")
        break
    else:
        print("Choix incorrect. Veuillez choisir une option valide (1-6).")

