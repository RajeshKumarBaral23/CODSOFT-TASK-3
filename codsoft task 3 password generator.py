import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters")
            return
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))
        password_label.config(text=f"Generated Password: {password}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

name_label = tk.Label(frame, text="Enter User Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

length_label = tk.Label(frame, text="Enter Password Length:")
length_label.grid(row=1, column=0, padx=10, pady=5)

length_entry = tk.Entry(frame)
length_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(frame, text="", fg="green", font=("bold", 15))
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()