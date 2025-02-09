import tkinter as tk
import subprocess
import sys
import os


class BananaBrainBoost:
    def __init__(self, root):
        self.root = root
        self.root.title("Banana Brain Boost")
        self.root.geometry("500x750")
        self.root.configure(bg="#ffeb99")
        
        # Main menu frame
        self.main_menu_frame = tk.Frame(root, bg="#ffeb99")
        self.main_menu_frame.pack(pady=100)

        self.title_label = tk.Label(self.main_menu_frame, text="Banana Brain Boost", font=("Arial", 24, "bold"), bg="#ffcc00", fg="#333")
        self.title_label.pack(pady=10)

        # Buttons for Start Game, Leaderboard, Profile, and Quit
        self.start_button = tk.Button(self.main_menu_frame, text="Start Game", font=("Arial", 14, "bold"), bg="#66cc66", fg="white", command=self.start_game)
        self.start_button.pack(pady=10, fill=tk.X)

        self.leaderboard_button = tk.Button(self.main_menu_frame, text="Leaderboard", font=("Arial", 14, "bold"), bg="#ffcc00", fg="black", command=self.show_leaderboard)
        self.leaderboard_button.pack(pady=10, fill=tk.X)

        self.profile_button = tk.Button(self.main_menu_frame, text="Profile", font=("Arial", 14, "bold"), bg="#3399ff", fg="white", command=self.show_profile)
        self.profile_button.pack(pady=10, fill=tk.X)

        self.quit_button = tk.Button(self.main_menu_frame, text="Quit", font=("Arial", 14, "bold"), bg="#ff6666", fg="white", command=self.quit_game)
        self.quit_button.pack(pady=10, fill=tk.X)

    # Fix: Define the method properly inside the class
    def start_game(self):
        self.root.destroy()  # Close the MainGUI window
        app_path = os.path.abspath("app.py")  # Get the absolute path of app.py
        subprocess.run([sys.executable, app_path])  # Run app.py

    def show_leaderboard(self):
        self.main_menu_frame.pack_forget()
        self.leaderboard_frame = tk.Frame(self.root, bg="#ffeb99")
        self.leaderboard_frame.pack(pady=20)
        self.leaderboard_label = tk.Label(self.leaderboard_frame, text="Leaderboard", font=("Arial", 18, "bold"), bg="#ffcc00", fg="#333")
        self.leaderboard_label.pack(pady=10)
        self.leaderboard_text = tk.Label(self.leaderboard_frame, text="1. Player One - 1000\n2. Player Two - 800\n3. Player Three - 600", font=("Arial", 14), bg="#ffeb99")
        self.leaderboard_text.pack(pady=10)
        self.quit_leaderboard_button = tk.Button(self.leaderboard_frame, text="Back to Main Menu", font=("Arial", 12), bg="#ffcc00", fg="black", command=self.go_back_to_main_menu)
        self.quit_leaderboard_button.pack(pady=20)

    def show_profile(self):
        self.main_menu_frame.pack_forget()
        self.profile_frame = tk.Frame(self.root, bg="#ffeb99")
        self.profile_frame.pack(pady=20)
        self.profile_label = tk.Label(self.profile_frame, text="Profile", font=("Arial", 18, "bold"), bg="#ffcc00", fg="#333")
        self.profile_label.pack(pady=10)
        self.profile_info = tk.Label(self.profile_frame, text="Username: Player One\nLevel: 5\nScore: 800", font=("Arial", 14), bg="#ffeb99")
        self.profile_info.pack(pady=10)
        self.quit_profile_button = tk.Button(self.profile_frame, text="Back to Main Menu", font=("Arial", 12), bg="#ffcc00", fg="black", command=self.go_back_to_main_menu)
        self.quit_profile_button.pack(pady=20)

    def quit_game(self):
        self.root.quit()

    def go_back_to_main_menu(self):
        if hasattr(self, 'game_frame'):
            self.game_frame.pack_forget()
        if hasattr(self, 'leaderboard_frame'):
            self.leaderboard_frame.pack_forget()
        if hasattr(self, 'profile_frame'):
            self.profile_frame.pack_forget()
        self.main_menu_frame.pack(pady=100)


if __name__ == "__main__":
    root = tk.Tk()
    game = BananaBrainBoost(root)
    root.mainloop()

