import re
import tkinter as tk
from tkinter import messagebox

# Common weak passwords
common_passwords = ["123456", "password", "qwerty", "admin", "hello123"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number")

    # Special character check
    if re.search(r'[!@#$%^&*(){}|<>?]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    # Common password check
    if password.lower() in common_passwords:
        suggestions.append("Avoid using common passwords")
        score = 1

    # Strength level
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


# Button click function
def analyze_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    strength, suggestions = check_password_strength(password)

    result_label.config(text=f"Password Strength: {strength}")

    suggestions_box.delete(1.0, tk.END)

    if suggestions:
        for suggestion in suggestions:
            suggestions_box.insert(tk.END, f"- {suggestion}\n")
    else:
        suggestions_box.insert(tk.END, "Your password is secure!")


# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password input
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, width=35, show="*", font=("Arial", 12))
password_entry.pack(pady=10)

# Check button
check_button = tk.Button(root, text="Check Strength", command=analyze_password)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Suggestions box
suggestions_box = tk.Text(root, height=10, width=50)
suggestions_box.pack(pady=10)

# Run app
root.mainloop()