def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def show_menu():
    print("\n--- Menu du Convertiseur de Temperature ---")
    print("1. Celsius vers Fahrenheit & Kelvin")
    print("2. Fahrenheit vers Celsius & Kelvin")
    print("3. Kelvin vers Celsius & Fahrenheit")
    print("4. Quitter")

while True:
    show_menu()
    choice = input("Votre choix (1-4): ")

    if choice == "1":
        celsius = float(input("Entrez la temperature en Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
        print(f"Kelvin: {celsius_to_kelvin(celsius):.2f}")
    elif choice == "2":
        fahrenheit = float(input("Entrez la temperature en Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}")
    elif choice == "3":
        kelvin = float(input("Entrez la temperature en Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(kelvin):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")
    elif choice == "4":
        print("Merci d'avoir utilisé le Convertisseur de Temperature !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide (1-4).")