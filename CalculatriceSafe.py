def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Vous ne pouvez pas diviser par 0.")
    return x / y

def show_menu():
    print("\n--- Menu ---")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

while True:
    show_menu()
    choice = input("Votre choix (1-5): ")

    if choice == "5":
        print("Merci d'avoir utilisé la Calculatrice !")
        break
    try:
        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxieme nombre: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Addition : {num1} + {num2} = {result}")
        elif choice == "2":
            result = substract(num1, num2)
            print(f"Soustraction : {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Multiplication : {num1} * {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Division : {num1} / {num2} = {result}")
        else:
            print("Choix invalide. Veuillez choisir une option valide (1-5).")
    except ValueError:
        print("Veuillez entrer des nombres valides.")
    except ZeroDivisionError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print("\n--- Merci d'avoir utilisé la calculatrice ---")