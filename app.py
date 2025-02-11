import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import subprocess
import sys
import os

class BananaBrainBoost:
    def __init__(self, root):
        self.root = root
        self.root.title("Banana Brain Boost Game")
        self.center_window(500, 700)
        self.root.configure(bg="#ffeb99")
        
        self.start_game()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def start_game(self):
        self.frame = tk.Frame(self.root, bg="#ffeb99")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.label = tk.Label(self.frame, text="Banana Brain Boost Game", font=("Arial", 18, "bold"), bg="#ffcc00", fg="#333")
        self.label.pack(pady=10, fill=tk.X)
        
        self.image_label = tk.Label(self.frame, bg="#ffeb99")
        self.image_label.pack(pady=10)
        
        self.quiz_label = tk.Label(self.frame, text="", font=("Arial", 14, "bold"), bg="#ffeb99")
        self.quiz_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(self.frame, font=("Arial", 14), justify="center", width=10)
        self.answer_entry.pack(pady=10)
        
        self.check_button = tk.Button(self.frame, text="Check", font=("Arial", 12, "bold"), bg="#66cc66", fg="white", command=self.check_answer)
        self.check_button.pack(pady=5)
        
        self.feedback_label = tk.Label(self.frame, text="", font=("Arial", 14, "bold"), bg="#ffeb99")
        self.feedback_label.pack(pady=10)
        
        self.next_button = tk.Button(self.frame, text="Next Question", font=("Arial", 12, "bold"), bg="#3399ff", fg="white", command=self.fetch_puzzle)
        self.next_button.pack(pady=5)
        
        self.timer_label = tk.Label(self.frame, text="Time left: 10s", font=("Arial", 12, "bold"), bg="#ffeb99")
        self.timer_label.pack(pady=5)
        
        self.back_button = tk.Button(self.frame, text="Go Back", font=("Arial", 12, "bold"), bg="#ff6666", fg="white", command=self.go_back)
        self.back_button.pack(pady=5)
        
        self.fetch_puzzle()

    def go_back(self):
        self.root.destroy()
        app_path = os.path.abspath("MainGUI.py")
        subprocess.run([sys.executable, app_path])

    def fetch_puzzle(self):
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php")
            data = response.json()
            if "question" in data and "solution" in data:
                self.correct_solution = int(data["solution"])
                self.quiz_label.config(text="Solve the puzzle shown in the image!")
                self.answer_entry.delete(0, tk.END)
                self.feedback_label.config(text="")
                self.start_timer()
                self.load_image(data["question"])
            else:
                self.feedback_label.config(text="Invalid puzzle data received.", fg="red")
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")

    def load_image(self, url):
        try:
            img_data = requests.get(url).content
            image = Image.open(BytesIO(img_data))
            image = image.resize((300, 300), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo
        except Exception as e:
            self.feedback_label.config(text="Error loading image", fg="red")

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_solution:
                self.feedback_label.config(text="Correct! 🎉", fg="green")
            else:
                self.feedback_label.config(text="Incorrect. Try again!", fg="red")
        except ValueError:
            self.feedback_label.config(text="Enter a valid number!", fg="red")

    def start_timer(self):
        self.time_left = 10
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.feedback_label.config(text="Time's up! Try again.", fg="red")
            self.fetch_puzzle()

if __name__ == "__main__":
    root = tk.Tk()
    game = BananaBrainBoost(root)
    root.mainloop()
