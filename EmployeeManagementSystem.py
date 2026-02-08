class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print("\n--- Information de l'employe ---")
        print(f"Identifiant: {self.emp_id}")
        print(f"Nom: {self.name}")
        print(f"Salaire: {self.salary}")

    def calculate_bonus(self):
        bonus = self.salary * 0.1
        return bonus
    

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Departement: {self.department}")

    def calculate_bonus(self):
        bonus = super().calculate_bonus() * 2
        return bonus
    
class Developper(Employee):
    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        self.language = language

    def display_info(self):
        super().display_info()
        print(f"Langage de programmation: {self.language}")
    
    def calculate_bonus(self):
        bonus = super().calculate_bonus() * 5
        return bonus
    
employees = []

def add_employee():
    print("\n--- Choisir le type d'employé ---")
    print("1. Employe")
    print("2. Manager")
    print("3. Developper")
    choice = int(input("Votre choix (1-3): ").strip())

    name = input("Nom de l'employé: ").strip()
    emp_id = input("Identifiant de l'employé: ").strip()
    salary = float(input("Salaire de l'employé: ").strip())

    if choice == 1:
        employees.append(Employee(name, emp_id, salary))
    elif choice == 2:
        department = input("Departement du manager: ").strip()
        employees.append(Manager(emp_id, name, salary, department))
    elif choice == 3:
        language = input("Langage de programmation du developpeur: ").strip()
        employees.append(Developper(emp_id, name, salary, language))
    else:
        print("Choix invalide. Veuillez choisir une option valide (1-3).")

def display_employees():
    print("\n--- Liste des employes ---")
    for employee in employees:
        employee.display_info()
        print(f"Bonus: {employee.calculate_bonus()}\n")


while True:
    print("\n--- Systeme de gestion des employes ---")
    print("1. Ajouter un employé")
    print("2. Afficher la liste des employes")
    print("3. Quitter")

    choice = int(input("Entrez votre choix (1-3): ").strip())

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_employees()
    elif choice == 3:
        print("Merci d'avoir utilisé le Systeme de gestion des employes !")
        break
    else:
        print(choice)
        print("Choix incorrect. Veuillez choisir une option valide.")