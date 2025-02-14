import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    # Here you would typically check the username and password
    if username and password:  # Simple validation
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Please enter both username and password.")

def create_account():
    messagebox.showinfo("Create Account", "Redirecting to account creation...")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Redirecting to password recovery...")

# Create the main window
root = tk.Tk()
root.title("Banana Brain Boost Login")
root.geometry("500x750")
root.configure(bg="#ffeb3b")  # Light yellow background

# Logo (Placeholder)
logo_label = tk.Label(root, text="Banana Brain Boost", font=("Arial", 24, "bold"), bg="#ffeb3b")
logo_label.pack(pady=20)

# Username Label and Entry
label_username = tk.Label(root, text="Username/Email", bg="#ffeb3b")
label_username.pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

# Password Label and Entry
label_password = tk.Label(root, text="Password", bg="#ffeb3b")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

# Show Password Checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, bg="#ffeb3b",
                                         command=lambda: entry_password.config(show='' if show_password_var.get() else '*'))
show_password_checkbox.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login, bg="#4caf50", fg="white", width=15)
login_button.pack(pady=20)

# Create Account Button
create_account_button = tk.Button(root, text="Create an Account", command=create_account, bg="#2196f3", fg="white", width=20)
create_account_button.pack(pady=5)

# Forgot Password Link
forgot_password_link = tk.Button(root, text="Forgot Password?", command=forgot_password, bg="#ffeb3b", fg="#d32f2f", relief='flat')
forgot_password_link.pack(pady=5)

# Footer
footer_label = tk.Label(root, text="© 2023 Banana Brain Boost", bg="#ffeb3b")
footer_label.pack(side='bottom', pady=10)

# Run the application
root.mainloop()