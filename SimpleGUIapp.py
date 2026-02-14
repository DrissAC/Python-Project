import tkinter as tk

root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x450")
root.config(bg="#f0f0f0")

is_dark_mode = False

traductions = {
    "Francais": {
        "titre": "Bienvenue sur mon APP GUI",
        "nom": "Entrez votre nom :",
        "greet": "Salut",
        "reset": "Réinitialiser",
        "success": "Salut, {} !",
        "error": "Veuillez entrer votre nom."
    },
    "English": {
        "titre": "Welcome to my GUI APP",
        "nom": "Enter your name:",
        "greet": "Greet",
        "reset": "Reset",
        "success": "Hello, {} !",
        "error": "Please enter your name."
    },
    "Espagnol": {
        "titre": "Bienvenido a mi APP",
        "nom": "Introduce tu nombre:",
        "greet": "Hola",
        "reset": "Reiniciar",
        "success": "¡Hola, {} !",
        "error": "Por favor, introduce tu nombre."
    },
    "日本語": {
        "titre": "GUIアプリへようこそ",
        "nom": "名前を入力してください :",
        "greet": "挨拶する",
        "reset": "リセット",
        "success": "こんにちは {} さん！",
        "error": "あなたの名前を入力してください."
    }
}

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    bg_color = "#2d2d2d" if is_dark_mode else "#f0f0f0"
    fg_color = "white" if is_dark_mode else "black"

    root.config(bg=bg_color)
    for label in [title_label, name_label, greeting_label]:
        label.config(bg=bg_color, fg=fg_color)
    
    update_language()
def update_language(*args):
    langue = variable.get()
    if langue in traductions:
        t = traductions[langue]
        title_label.config(text=t["titre"])
        name_label.config(text=t["nom"])
        greet_button.config(text=t["greet"])
        reset_button.config(text=t["reset"])
        greeting_label.config(text="")

def greet_user():
    name = name_entry.get()
    langue = variable.get()
    
    if langue not in traductions:
        greeting_label.config(text="Choisissez une langue / Select a language", fg="blue")
        return

    t = traductions[langue]
    if name:
        greeting_label.config(text=t["success"].format(name), fg="green")
    else:
        greeting_label.config(text=t["error"], fg="red")

def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")


title_label = tk.Label(root, text="Bienvenue sur mon APP GUI", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=20)

name_label = tk.Label(root, text="Entrez votre nom :", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

variable = tk.StringVar(root)
variable.set("Francais")
variable.trace_add("write", update_language)

options = list(traductions.keys())
dropdown = tk.OptionMenu(root, variable, *options)
dropdown.pack(pady=10)

greet_button = tk.Button(root, text="Salut", font=("Arial", 12), bg="#4CAF50", fg="white", command=greet_user)
greet_button.pack(pady=10)

reset_button = tk.Button(root, text="Réinitialiser", font=("Arial", 12), bg="#f44336", fg="white", command=reset)
reset_button.pack(pady=5)

theme_button = tk.Button(root, text="💡", font=("Arial", 10), command=toggle_theme)
theme_button.pack(pady=20)

greeting_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
greeting_label.pack(pady=20)

update_language()

root.mainloop()