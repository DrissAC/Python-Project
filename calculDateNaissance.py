
from datetime import date

name = input("Quel est votre nom? ")
date_naissance = (input("Quel est votre date de naissance (JJ/MM/AAAA)? "))
color = input("Quel est votre couleur preférée? ")

date_actuelle = date.today()
jour, mois, annee = date_naissance.split('/')
jour = int(jour)  
mois = int(mois)
annee = int(annee)

age = date_actuelle.year - annee -((date_actuelle.month, date_actuelle.day) < (mois, jour))
print("\n--- Bienvenue !!! ---")
print(f"Bonjour,{name} !")
print(f"Vous avez {age} ans.")
print(f"Votre couleur préférée est le {color}, c'est une belle couleur !.")

print("\n--- A bientôt !!! ---")