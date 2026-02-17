import tkinter as tk
import time
import sys

root = tk.Tk()
root.title("Click Counter")
root.geometry("400x500")
root.configure(bg="#e3f2fd")

counter = 0
total_seconds = 0.0
running = True

def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

def decrement():
    global counter
    counter -= 1
    counter_label.config(text=f"Clicks: {counter}")

def reset():
    global counter
    counter = 0
    counter_label.config(text=f"Clicks: {counter}")

def update_clock():
    global total_seconds
    if running:
        total_seconds += 0.1

        mins, reste = divmod(total_seconds, 60)
        secs, reste = divmod(reste, 1)
        formatted_time = f"{int(mins):02d}:{int(secs):02d}"

        stopwatch_label.config(text=f"Temps: {formatted_time}")
        root.after(100, update_clock)

stopwatch_label = tk.Label(root, text="Temps : 00:00.0", font=("Arial", 20, "bold"), bg="#e3f2fd", fg="#1565c0")
stopwatch_label.pack(pady=20)

title_label = tk.Label(root, text="Compteur de clicks", font=("Arial", 20), bg="#e3f2fd")
title_label.pack(pady=20)

counter_label = tk.Label(root, text=f"Clicks: 0", font=("Arial", 16), bg="#e3f2fd")
counter_label.pack(pady=10)

increment_button = tk.Button(root, text="Cliquez ici pour augmenter", font=("Arial", 14), bg="#4CAF50", fg="black", command=increment)
increment_button.pack(pady=10)

decrement_button = tk.Button(root, text="Cliquez ici pour diminuer", font=("Arial", 14), bg="#f44336", fg="black", command=decrement)
decrement_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), bg="#000000", fg="white", command=reset)
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Quitter", font=("Arial", 14), bg="#ffffff", fg="black", command=root.quit)
exit_button.pack(pady=10)

update_clock()

root.mainloop()