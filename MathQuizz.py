import random

def generer_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1,10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        reponse = num1 + num2
    elif operator == '-':
        reponse = num1 - num2
    elif operator == '*':
        reponse = num1 * num2

    return f"{num1} {operator} {num2}", reponse

def mathquizz():
    score = 0
    rounds = int(input("Combien de questions voulez-vous ? "))

    print("\n--- Bienvenue au Math Quizz ---")
    print(f"Vous serez face à {rounds} questions de mathématiques. A vous de donnez les bonnes réponses, Bonne chance !")

    for i in range(rounds):
        question, bonne_reponse = generer_question()
        print(f"\nQuestion {i + 1}: {question}")
        reponse_utilisateur = int(input("Votre réponse : "))
        
        if reponse_utilisateur == bonne_reponse:
            print("Bravo, bonne réponse !")
            score += 1
        else:
            print(f"Dommage, la bonne réponse est {bonne_reponse}")

    print("\n--- Fin du Math Quizz ---")
    print(f"Votre score est de {score}/{rounds}")

    if score == rounds:
        print("Bravo, vous avez gagné le Math Quizz !")
    elif score >= rounds // 2:
        print("Vous avez passé le Math Quizz, mais vous pouvez encore améliorer votre apprentissage.")
    else:
        print("Dommage, vous avez perdu le Math Quizz.")

    print("\n--- A bientôt !!! ---")

mathquizz()