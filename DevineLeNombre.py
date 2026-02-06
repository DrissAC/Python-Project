import random

secret_number = random.randint(1, 10)
attemps = 3

print("Je pense à un nombre entre 1 et 10")

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