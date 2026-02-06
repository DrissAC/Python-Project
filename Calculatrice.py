chiffre1 = float(input("Donnez un chiffre : "))
chiffre2 = float(input("Donnez un deuxieme chiffre : "))

Addition = chiffre1 + chiffre2
Soustraction = chiffre1 - chiffre2
Multiplication = chiffre1 * chiffre2
Division = chiffre1 / chiffre2

print("Choisissez une operation : ")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = 0

while choix not in [1, 2, 3, 4]:
    choix = int(input("Votre choix : "))

    if choix == 1:
        print(f"Addition : {chiffre1} + {chiffre2} = {Addition}")
        break
    elif choix == 2:
        print(f"Soustraction : {chiffre1} - {chiffre2} = {Soustraction}")
        break
    elif choix == 3:
        print(f"Multiplication : {chiffre1} * {chiffre2} = {Multiplication}")
        break
    elif choix == 4:
        print(f"Division : {chiffre1} / {chiffre2} = {Division}")
        break
    else:
        print("Choix invalide, recommencez !")