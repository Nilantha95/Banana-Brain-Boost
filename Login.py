import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
import sqlite3
from pathlib import Path

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Banana Puzzle Game - Login")
        
        # Match the window size from Start.py
        window_width = 500
        window_height = 750
        
        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
        
        self.root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
        
        # Load and setup background
        self.setup_background()
        
        # Create translucent overlay
        self.create_translucent_frame()
        
        # Add login components
        self.create_login_components()
        
        # Initialize database
        self.init_database()
    
    def setup_background(self):
        """Setup the background image"""
        self.bg_image = Image.open(r"Image Folder\monkey.webp")
        self.bg_image = self.bg_image.resize((500, 750), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

    def create_translucent_frame(self):
        """Create a translucent frame using PIL"""
        # Create a transparent overlay image
        overlay = Image.new('RGBA', (300, 400), (255, 215, 0, 128))  # Semi-transparent yellow
        self.overlay_image = ImageTk.PhotoImage(overlay)
        
        # Create a label with the overlay image
        self.overlay_label = tk.Label(self.root, image=self.overlay_image)
        self.overlay_label.place(relx=0.5, rely=0.4, anchor='center')
        
        # Create a frame for the login components
        self.login_frame = tk.Frame(self.root, bd=0)
        self.login_frame.place(relx=0.5, rely=0.4, anchor='center', width=300, height=400)

    def create_login_components(self):
        """Create all login UI components"""
        # Login Title
        self.title_label = tk.Label(
            self.login_frame,
            text="Player Login",
            font=("Arial", 24, "bold"),
            bg=self.root.cget('bg'),
            fg='black'
        )
        self.title_label.pack(pady=20)
        
        # Email Entry
        self.email_frame = tk.Frame(self.login_frame, bg=self.root.cget('bg'))
        self.email_frame.pack(pady=10)
        
        self.email_label = tk.Label(
            self.email_frame,
            text="Email:",
            font=("Arial", 12),
            bg=self.root.cget('bg'),
            fg='black'
        )
        self.email_label.pack(anchor='w')
        
        self.email_entry = tk.Entry(
            self.email_frame,
            font=("Arial", 12),
            width=25,
            bd=2,
            relief="groove"
        )
        self.email_entry.pack()
        
        # Password Entry
        self.password_frame = tk.Frame(self.login_frame, bg=self.root.cget('bg'))
        self.password_frame.pack(pady=10)
        
        self.password_label = tk.Label(
            self.password_frame,
            text="Password:",
            font=("Arial", 12),
            bg=self.root.cget('bg'),
            fg='black'
        )
        self.password_label.pack(anchor='w')
        
        self.password_entry = tk.Entry(
            self.password_frame,
            font=("Arial", 12),
            width=25,
            bd=2,
            relief="groove",
            show="*"
        )
        self.password_entry.pack()
        
        # Login Button
        self.login_button = tk.Button(
            self.login_frame,
            text="Login",
            font=("Arial", 14, "bold"),
            bg="black",
            fg="white",
            width=15,
            height=1,
            relief="flat",
            command=self.login
        )
        self.login_button.pack(pady=20)
        
        # Reset Password Link
        self.reset_password = tk.Label(
            self.login_frame,
            text="Reset Your Password?",
            font=("Arial", 10, "underline"),
            bg=self.root.cget('bg'),
            fg='blue',
            cursor="hand2"
        )
        self.reset_password.pack()
        self.reset_password.bind('<Button-1>', self.reset_password_click)
        
        # Create Account Link
        self.create_account = tk.Label(
            self.login_frame,
            text="Create a new User Account?",
            font=("Arial", 10, "underline"),
            bg=self.root.cget('bg'),
            fg='blue',
            cursor="hand2"
        )
        self.create_account.pack(pady=10)
        self.create_account.bind('<Button-1>', self.create_account_click)

    def init_database(self):
        """Initialize SQLite database for user management"""
        db_path = Path("database/users.db")
        db_path.parent.mkdir(exist_ok=True)
        
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        # Create users table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def login(self):
        """Handle login button click"""
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        # Check credentials in database
        self.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cursor.fetchone()
        
        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # Close login window
            # Start the main game window here
            game_root = tk.Tk()
            from Start import BananaPuzzleGame  # Import the main game class
            game = BananaPuzzleGame(game_root)
            game_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid email or password")
    
    def reset_password_click(self, event):
        """Handle reset password link click"""
        messagebox.showinfo("Reset Password", "Password reset functionality will be implemented here")
    
    def create_account_click(self, event):
        """Handle create account link click"""
        messagebox.showinfo("Create Account", "Account creation functionality will be implemented here")
    
    def __del__(self):
        """Close database connection when object is destroyed"""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    login = LoginUI(root)
    root.mainloop()
