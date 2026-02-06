import json
import os

TASK_FILE ='my_tasks.json'

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(task):
    task_name = input("Entrez le nom de la tache : ").strip()
    tasks = load_tasks()
    tasks.append({"task": task_name, "statuts": "Incomplete"})
    save_tasks(tasks)
    print(f"La tache {task_name} a bien ete ajoutee.")

def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- A faire ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} ({task['statuts']})")
    else:
        print("Aucune tache enregistrée.")

def update_status():
    tasks =load_tasks()
    view_tasks()
    try:
        task_index = int(input("Entrez le numero de la tache : ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("Entrez le nouveau statut (Complete/Incomplete) : ").strip()
            tasks[task_index]["statuts"] = new_status
            save_tasks(tasks)
            print(f"Le statut de la tache {tasks[task_index]['task']} a bien ete mis à jour.")
        else:
            print("Numero de tache invalide.")
    except ValueError:
        print("Entrez un numero de tache valide.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Entrez le numero de la tache a supprimer : ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"La tache {deleted_task['task']} a bien ete supprimée.")
        else:
            print("Numero de tache invalide.")
    except ValueError:
        print("Entrez un numero de tache valide.")


def display_menu():
    print("\n--- Menu ---")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Modifier le statut d'une tache")
    print("4. Supprimer une tache")
    print("5. Quitter")

while True:
    display_menu()
    choice = input("Votre choix (1-5): ").strip()

    if choice == "1":
        add_task(choice)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Merci d'avoir utilisé la To-Do App ! Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide (1-5).")  