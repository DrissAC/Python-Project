import tkinter as tk

root = tk.Tk()
root.title("Button State Management")
root.geometry("300x200")

def toogle_button():
    if button['state'] == 'normal':
        button.config(state='disabled')
        toggle_btn.config(text='Enable Button')
    else:
        button.config(state='normal')
        toggle_btn.config(text='Disable Button')

button = tk.Button(root, text="I am Active")
button.pack(pady=10)

toggle_btn = tk.Button(root, text="Disable Button", command=toogle_button)
toggle_btn.pack(pady=10)

root.mainloop()