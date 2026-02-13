class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self._pin = pin
        self._balance = balance

    def validate_pin(self, entered_pin):
        return entered_pin == self._pin
    
    def check_balance(self):
        print(f"Solde: {self._balance}€")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Depot de {amount}€. Nouveau solde: {self._balance}€")
        else:
            print("Montant incorrect, cela doit etre superieur a 0.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Solde insuffisant.")
        elif amount > 0:
            self._balance -= amount
            print(f"Retrait de {amount}€. Nouveau solde: {self._balance}€")
        else:
            print("Montant incorrect, cela doit etre superieur a 0.")

    def change_pin(self, old_pin,new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self._pin = new_pin
            print("PIN modifie avec succes.")
        else:
            print("PIN incorrect ou format incorrect.")

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self):
        account_number = input("Entrez le numero de compte: ")
        pin = input("Entrez le PIN a 4 chiffres: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Compte cree avec succes.")
        else:
            print("PIN incorrect ou format incorrect.")

    def authenticate_account(self):
        account_number = input("Entrez le numero de compte: ")
        pin = input("Entrez le PIN: ")

        account = self.accounts.get(account_number)
        if account and account.validate_pin(pin):
            print("Authentification reussie.")
            self.account_menu(account)
        else:
            print("Authentification echouee.")

    def account_menu(self, account):
        while True:
            print("\n--- Menu du compte ---")
            print("1. Verifier le solde")
            print("2. Depot")
            print("3. Retrait")
            print("4. Changer le PIN")
            print("5. Quitter")

            choice = input("Entrez votre choix (1-5): ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = float(input("Entrez le montant du depot: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Entrez le montant du retrait: "))
                account.withdraw(amount)
            elif choice == "4":
                old_pin = input("Entrez le PIN actuel: ")
                new_pin = input("Entrez le nouveau PIN a 4 chiffres: ")
                account.change_pin(old_pin, new_pin)
            elif choice == "5":
                print("Deconnexion...")
                break
            else:
                print("Choix incorrect. Veuillez choisir une option valide. (1-5)")

    def main_menu(self):
        while True:
            print("\n--- ATM ---")
            print("1. Ajouter un compte")
            print("2. Authentifier un compte")
            print("3. Quitter")

            choice = input("Entrez votre choix (1-3): ")

            if choice == "1":
                self.add_account()
            elif choice == "2":
                self.authenticate_account()
            elif choice == "3":
                print("Merci d'avoir utilisé l'ATM !")
                break
            else:
                print("Choix incorrect. Veuillez choisir une option valide (1-3).")

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()