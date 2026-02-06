a = float(input("Donnez un nombre : "))
b = float(input("Donnez un deuxieme nombre : "))

print("\n--- Comparaison entre deux nombres ---")
if a == b:
    print(f"{a} et {b} sont identiques")
elif a > b:
    print(f"{a} est plus grand que {b}")
else:
    print(f"{a} est plus petit que {b}")

if a == 0 or b == 0:
    print("Un des deux nombres est nul")
else:
    print("Aucun des deux nombres n'est nul")