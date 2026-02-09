class Animal:
    def make_sound(self):
        print("Son d'animal par defaut")

class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

class Cat(Animal):
    def make_sound(self):
        print("Miaou miaou")

class Vache(Animal):
    def make_sound(self):
        print("Meuh meuh")

class Canard(Animal):
    def make_sound(self):
        print("Coin coin")

class AnimalSoundSimulator:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.__class__.__name__} a bien ete ajouté.")
        else:
            print("Animal incorrect.")
    
    def make_all_sounds(self):
        if not self.animals:
            print("Aucun animal dans le simulateur.")

        else:
            print("\n--- Sons des animaux ---")
            for animal in self.animals:
                animal.make_sound()

simulator =AnimalSoundSimulator()


while True:
    print("\n--- Simulateur de son d'animaux ---")
    print("1. Ajouter un chien")
    print("2. Ajouter un chat")
    print("3. Ajouter une vache")
    print("4. Ajouter un canard")
    print("5. Jouer les sons des animaux")
    print("6. Quitter")

    choice = input("Entrez votre choix (1-6): ").strip()

    if choice == "1":
        simulator.add_animal(Dog())
    elif choice == "2":
        simulator.add_animal(Cat())
    elif choice == "3":
        simulator.add_animal(Vache())
    elif choice == "4":
        simulator.add_animal(Canard())
    elif choice == "5":
        simulator.make_all_sounds()
    elif choice == "6":
        print("Merci d'avoir utilisé le Simulateur de son d'animaux !")
        break
    else:
        print("Choix incorrect. Veuillez choisir une option valide.")