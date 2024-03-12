import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        
        length_label = ttk.Label(self.root, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.length_entry = ttk.Entry(self.root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        
        self.lowercase_var = tk.BooleanVar()
        lowercase_check = ttk.Checkbutton(self.root, text="Include Lowercase", variable=self.lowercase_var)
        lowercase_check.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W)

        self.uppercase_var = tk.BooleanVar()
        uppercase_check = ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.uppercase_var)
        uppercase_check.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W)

        self.digits_var = tk.BooleanVar()
        digits_check = ttk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var)
        digits_check.grid(row=3, column=0, columnspan=2, pady=5, sticky=tk.W)

        self.symbols_var = tk.BooleanVar()
        symbols_check = ttk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var)
        symbols_check.grid(row=4, column=0, columnspan=2, pady=5, sticky=tk.W)

        
        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_lowercase = self.lowercase_var.get()
            use_uppercase = self.uppercase_var.get()
            use_digits = self.digits_var.get()
            use_symbols = self.symbols_var.get()

            characters = ""
            if use_lowercase:
                characters += string.ascii_lowercase
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_digits:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation

            if not characters:
                messagebox.showwarning("Warning", "At least one character set must be selected.")
                return

            password = ''.join(secrets.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
