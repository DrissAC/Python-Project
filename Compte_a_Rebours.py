import time

start = int(input("Entrer le nombre pour commencer le compte a rebours : "))
vitesse = int(input("Entrer la vitesse de compte a rebours : "))
moitie = start // 2

print("\n--- le compte a rebours commence ---")
while start > 0:
    print(start)
    if start <= moitie and (start + vitesse) > moitie:
        print("Vous êtes a la moitie du compte a rebours")

    time.sleep(vitesse)
    start -= vitesse

print("\n--- le compte a rebours est fini !!! ---")