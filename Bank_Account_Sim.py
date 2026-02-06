class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depot de {amount}€. Nouveau solde: {self.balance}€")
        else:
            print("Montant incorrect, cela doit etre superieur a 0.")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Retrait de {amount}€. Nouveau solde: {self.balance}€")
        else:
            print("Montant incorrect ou solde insuffisant.")

    def show_details(self):
        print("\n--- Details du compte ---")
        print(f"Nom du titulaire du compte: {self.account_holder}")
        print(f"Solde: {self.balance}€")

accounts = {}

def create_account():
    name = input("Nom du titulaire du compte: ").strip()
    intial_deposit = float(input("Entrez le montant du depot initial: "))
    account = BankAccount(name, intial_deposit)
    accounts[name] = account
    print("\n--- Compte cree avec succes ! ---")

def access_account():
    name = input("Nom du titulaire du compte: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n--- Menu du compte ---")
            print("1. Depot")
            print("2. Retrait")
            print("3. Details du compte")
            print("4. Quitter")
            choice = input("Entrez votre choix (1-4): ")
            if choice == "1":
                amount = float(input("Entrez le montant du depot: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Entrez le montant du retrait: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_details()
            elif choice == "4":
                break
            else:
                print("Choix incorrect. Veuillez choisir une option valide.")


while True:
    print("\n--- Menu principal ---")
    print("1. Creation de compte")
    print("2. Acces au compte")
    print("3. Quitter")
    choice = input("Entrez votre choix (1-3): ")
    if choice == "1":
        create_account()
    elif choice == "2":
        access_account()
    elif choice == "3":
        print("Merci d'avoir utilisé la Banque !")
        break
    else:
        print("Choix incorrect. Veuillez choisir une option valide.")