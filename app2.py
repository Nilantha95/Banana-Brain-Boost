import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import random


class BananaPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Banana Puzzle Game")
        self.root.geometry("500x700")
        self.root.configure(bg="#ffeb99")
        
        self.frame = tk.Frame(root, bg="#ffeb99")
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="Banana Puzzle Game", font=("Arial", 18, "bold"), bg="#ffcc00", fg="#333")
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
        
        self.level = 1  # Start with level 1
        self.fetch_puzzle()
    
    def fetch_puzzle(self):
        # Based on level, fetch a different puzzle type from the API
        self.quiz_label.config(text="Solve the puzzle!")
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.start_timer()
        
        if self.level <= 3:
            self.fetch_addition_subtraction_puzzle()
        elif self.level <= 6:
            self.fetch_multiplication_division_puzzle()
        elif self.level <= 9:
            self.fetch_fractions_decimals_puzzle()
        else:
            self.fetch_algebraic_expressions_puzzle()
    
    def fetch_addition_subtraction_puzzle(self):
        # Level 1-3: Basic Addition & Subtraction
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=addition_subtraction")
            data = response.json()
            if "question" in data and "solution" in data:
                self.correct_solution = int(data["solution"])
                self.quiz_label.config(text=data["question"])
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def fetch_multiplication_division_puzzle(self):
        # Level 4-6: Multiplication & Division
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=multiplication_division")
            data = response.json()
            if "question" in data and "solution" in data:
                self.correct_solution = int(data["solution"])
                self.quiz_label.config(text=data["question"])
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def fetch_fractions_decimals_puzzle(self):
        # Level 7-9: Fractions & Decimals
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=fractions_decimals")
            data = response.json()
            if "question" in data and "solution" in data:
                self.correct_solution = round(float(data["solution"]), 2)
                self.quiz_label.config(text=data["question"])
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def fetch_algebraic_expressions_puzzle(self):
        # Level 10: Algebraic Expressions
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=algebraic_expressions")
            data = response.json()
            if "question" in data and "solution" in data:
                self.correct_solution = float(data["solution"])  # Assuming algebraic expressions return float solutions
                self.quiz_label.config(text=data["question"])
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def check_answer(self):
        try:
            user_answer = float(self.answer_entry.get())
            if user_answer == self.correct_solution:
                self.feedback_label.config(text="Correct! 🎉", fg="green")
                self.level += 1  # Move to the next level after a correct answer
                if self.level > 10:
                    self.feedback_label.config(text="You've completed all levels! 🎉", fg="green")
                    self.next_button.config(state=tk.DISABLED)  # Disable Next button at max level
            else:
                self.feedback_label.config(text="Incorrect. Try again!", fg="red")
        except ValueError:
            self.feedback_label.config(text="Enter a valid number!", fg="red")
    
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO


class BananaPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Banana Puzzle Game")
        self.root.geometry("500x700")
        self.root.configure(bg="#ffeb99")
        
        self.frame = tk.Frame(root, bg="#ffeb99")
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="Banana Puzzle Game", font=("Arial", 18, "bold"), bg="#ffcc00", fg="#333")
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
        
        self.level = 1  # Start with level 1
        self.fetch_puzzle()
    
    def fetch_puzzle(self):
        # Based on level, fetch a different puzzle type from the API
        self.quiz_label.config(text="Solve the puzzle!")
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.start_timer()
        
        if self.level <= 3:
            self.fetch_addition_subtraction_puzzle()
        elif self.level <= 6:
            self.fetch_multiplication_division_puzzle()
        elif self.level <= 9:
            self.fetch_fractions_decimals_puzzle()
        else:
            self.fetch_algebraic_expressions_puzzle()
    
    def fetch_addition_subtraction_puzzle(self):
        # Level 1-3: Basic Addition & Subtraction
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=addition_subtraction")
            data = response.json()
            print(data)  # Debugging line to check the full response
            if "question" in data and "solution" in data:
                # Check if the question is a URL or math question
                if data["question"].startswith("http"):  # If it starts with 'http', it's likely a URL
                    self.load_image(data["question"])  # Load image if the question is a URL
                else:
                    self.quiz_label.config(text=data["question"])  # Otherwise, display the math question
                self.correct_solution = int(data["solution"])
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def fetch_multiplication_division_puzzle(self):
        # Level 4-6: Multiplication & Division
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=multiplication_division")
            data = response.json()
            print(data)  # Debugging line to check the full response
            if "question" in data and "solution" in data:
                if data["question"].startswith("http"):
                    self.load_image(data["question"])
                else:
                    self.quiz_label.config(text=data["question"])
                self.correct_solution = int(data["solution"])
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def fetch_fractions_decimals_puzzle(self):
        # Level 7-9: Fractions & Decimals
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=fractions_decimals")
            data = response.json()
            print(data)  # Debugging line to check the full response
            if "question" in data and "solution" in data:
                if data["question"].startswith("http"):
                    self.load_image(data["question"])
                else:
                    self.quiz_label.config(text=data["question"])
                self.correct_solution = round(float(data["solution"]), 2)
        except Exception as e:
            self.feedback_label.config(text="Error fetching puzzle", fg="red")
    
    def fetch_algebraic_expressions_puzzle(self):
        # Level 10: Algebraic Expressions
        try:
            response = requests.get("https://marcconrad.com/uob/banana/api.php?type=algebraic_expressions")
            data = response.json()
            print(data)  # Debugging line to check the full response
            if "question" in data and "solution" in data:
                if data["question"].startswith("http"):
                    self.load_image(data["question"])
                else:
                    self.quiz_label.config(text=data["question"])
                self.correct_solution = float(data["solution"])
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
            user_answer = float(self.answer_entry.get())
            if user_answer == self.correct_solution:
                self.feedback_label.config(text="Correct! 🎉", fg="green")
                self.level += 1  # Move to the next level after a correct answer
                if self.level > 10:
                    self.feedback_label.config(text="You've completed all levels! 🎉", fg="green")
                    self.next_button.config(state=tk.DISABLED)  # Disable Next button at max level
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
    game = BananaPuzzleGame(root)
    root.mainloop()

