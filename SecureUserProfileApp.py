class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self._password = password
        self.set_password(password)

    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("Email mis a jour avec succes")
        else:
            print("Email incorrect")


    def set_password(self, password):
        if len(password) < 6:
            print("Le mot de passe doit contenir au moins 6 caractere")
            return
        else:
            self._password = password
            print("Le mot de passe a ete modifie avec succes")


    def display_profile(self):
        print("\n--- Profil de l'utilisateur ---")
        print(f"Nom d'utilisateur: {self.username}")
        print(f"Email: {self._email}")
        print(f"Mot de passe: {self._password}")

users = []

def create_user():
    username = input("Entrez le nom d'utilisateur: ")
    email = input("Entrez l'adresse email: ")
    password = input("Entrez le mot de passe: ")
    user = UserProfile(username, email, password)
    users.append(user)
    print("Utilisateur cree avec succes !")


def view_profiles():
    if not users:
        print("Aucun utilisateur trouve.")
    else:
        for user in users:
            user.display_profile()

def update_email():
    username = input("Entrez le nom de l'utilisateur: ")
    for user in users:
        if user.username == username:
            new_email = input("Entrez la nouvelle adresse email: ")
            user.set_email(new_email)
            return
    print("Utilisateur non trouve.")

def reset_password():
    username = input("Entrez le nom d'utilisateur: ")
    for user in users:
        if user.username == username:
            password = input("Entrez le nouveau mot de passe: ")
            user.set_password(password)
            return
    print("Utilisateur non trouve.")

while True:
    print("\n--- Menu principal ---")
    print("1. Créer un utilisateur")
    print("2. Afficher les profils")
    print("3. Mettre à jour l'email")
    print("4. Mettre à jour le mot de passe")
    print("5. Quitter")

    choice = input("Entrez votre choix (1-5): ")

    if choice == "1":
        create_user()
    elif choice == "2":
        view_profiles()
    elif choice == "3":
        update_email()
    elif choice == "4":
        reset_password()
    elif choice == "5":
        print("Merci d'avoir utilisé l'application !")
        break
    else:
        print("Choix incorrect. Veuillez choisir une option valide (1-5).")