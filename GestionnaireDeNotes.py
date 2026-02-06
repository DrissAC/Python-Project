notes_etudiants = input("Entrez les notes des etudiants (separees par des espaces) : ")

notes = [int(note) for note in notes_etudiants.split(",")]

grades =[
    "A" if note >= 90 else
    "B" if note >= 80 else
    "C" if note >= 70 else
    "D" if note >= 60 else
    "F"
    for note in notes
]

reussi = [note for note in notes if note >= 60]
echoue = [note for note in notes if note < 60]

print("\n--- Notes des etudiants ---")

for i, (note, grades) in enumerate(zip(notes,grades), start=1):
    print(f"Etudiant {i}: Notes = {note} -> Mention: {grades}")

print("\n--- Etudiants qui ont reussis ou echoues ---")
print(f"Etudiants qui ont reussis : {reussi}")
print(f"Etudiants qui ont echoues : {echoue}")