import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import PIL for handling images

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Please enter both username and password.")

def create_account():
    messagebox.showinfo("Create Account", "Redirecting to account creation...")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Redirecting to password recovery...")

def animate_text():
    words = ["Banana", "Brain", "Boost"]
    label_text.set("")  # Clear the label initially
    y_pos = -50  # Start above the window
    
    def move_word(index=0, y=y_pos):
        if index < len(words):
            label_text.set(" ".join(words[:index+1]))  # Show words one by one
            heading_label.place(x=70, y=y)  # Move down
            if y < 50:  # Move down until it reaches the final position
                root.after(50, move_word, index, y + 5)  
            else:
                root.after(500, move_word, index + 1, -50)  # Start next word
    
    move_word()

# Create the main window
root = tk.Tk()
root.title("Banana Brain Boost Login")
root.geometry("500x750")

# Load background image
bg_image = Image.open(r"Image Folder\monkey2.webp")  # Updated file path
bg_image = bg_image.resize((500, 750))  # Resize to match window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Frame for centering content
frame = tk.Frame(root, bg=root.cget("bg"), bd=5)  # Match parent background
frame.place(relx=0.5, rely=0.5, anchor="center")

# Animated Heading Label
label_text = tk.StringVar()
heading_label = tk.Label(root, textvariable=label_text, font=("Comic Sans MS", 26, "bold"), fg="#ff5722", bg=root.cget("bg"))  # Match background
heading_label.place(x=70, y=-50)  # Start above window

# Start animation
root.after(500, animate_text)

# Username Label and Entry
label_username = tk.Label(frame, text="Username/Email", font=("Arial", 12, "bold"), bg=root.cget("bg"), fg="#333")  # Match background
label_username.pack(anchor="w", padx=20, pady=(20, 5))
entry_username = tk.Entry(frame, font=("Arial", 14), width=30, relief="solid", bd=2, fg="#333", highlightbackground=root.cget("bg"))
entry_username.pack(pady=(5, 15))

# Password Label and Entry
label_password = tk.Label(frame, text="Password", font=("Arial", 12, "bold"), bg=root.cget("bg"), fg="#333")  # Match background
label_password.pack(anchor="w", padx=20, pady=(10, 5))
entry_password = tk.Entry(frame, font=("Arial", 14), width=30, show="*", relief="solid", bd=2, fg="#333", highlightbackground=root.cget("bg"))
entry_password.pack(pady=(5, 15))

# Show Password Checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(
    frame, text="Show Password", variable=show_password_var, bg=root.cget("bg"),
    command=lambda: entry_password.config(show='' if show_password_var.get() else '*'), 
    font=("Arial", 10)
)
show_password_checkbox.pack(pady=10)

# Login Button
login_button = tk.Button(frame, text="Login", command=login, bg="#4caf50", fg="white", width=15, font=("Arial", 12, "bold"), relief="flat")
login_button.pack(pady=15)

# Create Account Button
create_account_button = tk.Button(frame, text="Create an Account", command=create_account, bg="#2196f3", fg="white", width=20, font=("Arial", 12, "bold"), relief="flat")
create_account_button.pack(pady=10)

# Forgot Password Link
forgot_password_link = tk.Button(frame, text="Forgot Password?", command=forgot_password, bg=root.cget("bg"), fg="#d32f2f", relief='flat', font=("Arial", 10, "italic"))
forgot_password_link.pack(pady=5)

# Footer
footer_label = tk.Label(root, text="© 2025 Banana Brain Boost", bg=root.cget("bg"), font=("Arial", 8))  # Match background
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()


