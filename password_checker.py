import re
import tkinter as tk
from tkinter import messagebox

def password_strength_checker(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None  # \W represents anything that is not a letter or a number

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    missing_criteria = []
    if not length_criteria:
        missing_criteria.append("• At least 8 characters")
    if not uppercase_criteria:
        missing_criteria.append("• An uppercase letter")
    if not lowercase_criteria:
        missing_criteria.append("• A lowercase letters")
    if not number_criteria:
        missing_criteria.append("• A number")
    if not special_char_criteria:
        missing_criteria.append("• A special character")

    if score == 5:
        return "Very strong", []
    else:
        missing_text = '\n'.join(missing_criteria)
        return f"{['Very weak', 'Weak', 'Moderate', 'Strong'][score-1]}", f"Missing:\n{missing_text}"

def check_password():
    password = entry.get()
    strength, feedback = password_strength_checker(password)
    result_label.config(text=f"Strength: {strength}")
    if feedback:
        feedback_label.config(text=feedback)
    else:
        feedback_label.config(text="")

window = tk.Tk()
window.title("Password Strength Checker")

window.geometry("500x300")
window.config(bg="#ADD8E6")  # Light blue color

label = tk.Label(window, text="Enter your password:", bg="#ADD8E6", fg="yellow", font=("Arial", 12, "bold"))
label.pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack()

check_button = tk.Button(window, text="Check", command=check_password, bg="yellow", fg="#000080", font=("Arial", 10, "bold"))  # Dark blue text
check_button.pack(pady=10)

result_label = tk.Label(window, text="", bg="#ADD8E6", fg="#000080", font=("Arial", 12))
result_label.pack()

feedback_label = tk.Label(window, text="", bg="#ADD8E6", fg="#333333", font=("Arial", 10), justify="left")
feedback_label.pack(pady=10)

window.mainloop()

