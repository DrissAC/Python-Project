import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("IMC Calculateur")
root.geometry("400x400")
root.configure(bg="#f0f4c3")

title_label = tk.Label(root, text="Calcutateur de IMC", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

weight_label = tk.Label(root, text="Poids (kg):", font=("Arial", 12), bg="#f0f4c3")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12), width=15)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Taille (m):", font=("Arial", 12), bg="#f0f4c3")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 12), width=15)
height_entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4c3")
result_label.pack(pady=20)

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Veuillez entrer des valeurs valides.")
        
        bmi = weight / (height ** 2)
        result_label.config(text=f"Votre IMC est de : {bmi:.2f}")
        status = ""
        if bmi < 18.5:
            status = "sous poids"
        elif 18.5 <= bmi < 25:
            status = "poids normal"
        elif 25 <= bmi < 30:
            status = "surpoids"
        else:
            status = "obesite"
        result_label.config(text=f"Votre IMC est de : {bmi:.2f} ({status})", fg="green")
    except ValueError as e:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides : " + str(e))

calculate_button = tk.Button(root, text="Calculer IMC", font=("Arial", 12), command=calculate_bmi)
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=lambda: (weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="")))
reset_button.pack(pady=10)

root.mainloop()