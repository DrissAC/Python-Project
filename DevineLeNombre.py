import random


print(f"\n--- Bienvenue au jeu 'Devine le Nombre' ---")
while True:
    choose_secret_number = int(input("Choississez un nombre secret : ").strip())
    print(f"Vous avez choisi {choose_secret_number}, je vais penser a un nombre entre 1 et {choose_secret_number}, a vous de le deviner !")
    secret_number = random.randint(1, choose_secret_number)
    attemps = int (input("Combien d'essais voulez-vous ? : "))

    print(f"Je pense à un nombre entre 1 et {choose_secret_number}, vous avez {attemps} essais !")

    while attemps > 0: 
        guess = int(input("Pouvez-vous le devinez ?: "))
        if guess == secret_number:
            print("Bravo, vous avez gagné")
            break
        elif guess > secret_number:
            print("C'est moins")
            attemps -= 1
        else:
            print("C'est plus")
            attemps -= 1

    if attemps == 0:
        print("Dommage, vous avez perdu, le nombre secret était", secret_number)

    play_again = input("Voulez-vous jouer encore ? (o/n) : ").strip().lower()
    if play_again != "o":
        print("Merci d'avoir joué !")
        break