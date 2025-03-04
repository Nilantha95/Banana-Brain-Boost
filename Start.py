import tkinter as tk
from PIL import Image, ImageTk
import pygame
import subprocess
import sys
import os

class BananaPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Banana Puzzle Game")
        
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set the window size
        window_width = 500
        window_height = 750

        # Calculate the position to center the window
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)

        # Set the window geometry to center it
        self.root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        # Initialize pygame mixer for audio
        pygame.mixer.init()
        self.music_playing = True  # Track if music is playing
        self.music_file = r"Music Folder\byte-blast-8-bit-arcade-music-background-music-for-video-208780.mp3"

        
        # Start playing background music
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)  # Loop indefinitely

        # Load Background Image
        self.bg_image = Image.open(r"Image Folder\monkey.webp")
        self.bg_image = self.bg_image.resize((500, 750), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Load and Resize Button Images
        self.start_button_img = Image.open(r"Image Folder/Screenshot 2025-02-14 200242.png").resize((170, 60), Image.Resampling.LANCZOS)
        self.leaderboard_button_img = Image.open(r"Image Folder\Screenshot 2025-02-14 173044.png").resize((170, 60), Image.Resampling.LANCZOS)
        self.profile_button_img = Image.open(r"Image Folder\Screenshot 2025-02-14 200035.png").resize((170, 60), Image.Resampling.LANCZOS)
        self.quit_button_img = Image.open(r"Image Folder\Screenshot 2025-02-14 200149.png").resize((170, 60), Image.Resampling.LANCZOS)

        # Convert images to PhotoImage format
        self.start_photo = ImageTk.PhotoImage(self.start_button_img)
        self.leaderboard_photo = ImageTk.PhotoImage(self.leaderboard_button_img)
        self.profile_photo = ImageTk.PhotoImage(self.profile_button_img)
        self.quit_photo = ImageTk.PhotoImage(self.quit_button_img)

        # Place Buttons in the Center
        button_y_offset = 200  
        button_spacing = 80  

        self.start_button = tk.Button(root, image=self.start_photo, borderwidth=0, command=self.start_game)
        self.start_button.place(x=175, y=button_y_offset)

        self.leaderboard_button = tk.Button(root, image=self.leaderboard_photo, borderwidth=0, command=self.show_leaderboard)
        self.leaderboard_button.place(x=175, y=button_y_offset + button_spacing)

        self.profile_button = tk.Button(root, image=self.profile_photo, borderwidth=0, command=self.show_profile)
        self.profile_button.place(x=175, y=button_y_offset + 2 * button_spacing)

        self.quit_button = tk.Button(root, image=self.quit_photo, borderwidth=0, command=self.quit_game)
        self.quit_button.place(x=175, y=button_y_offset + 3 * button_spacing)

        # Add an Attractive, Rounded Music Toggle Button at the bottom
        self.music_button = tk.Button(
            root, 
            text="Mute Music", 
            width=15, 
            height=2, 
            command=self.toggle_music, 
            bg="yellow",  # Yellow background
            fg="black",  # Black text color
            font=("Arial", 14, "bold"),  # Bold, readable font
            relief="flat",  # Flat relief style for smooth edges
            borderwidth=2,  # Slight border for the button
            activebackground="orange",  # Color when clicked
            activeforeground="black",  # Text color when clicked
            highlightthickness=0,  # Remove focus border
            bd=0,  # Remove button border
            padx=20,  # Add horizontal padding
            pady=10  # Add vertical padding
        )
        self.music_button.place(x=160, y=650)  # Position it near the bottom

    def start_game(self):
     pygame.mixer.music.stop()
     self.root.destroy()  # Close the start screen
     app_path = os.path.abspath("app.py")  # Get the absolute path of app.py
     subprocess.run([sys.executable, app_path])  # Run app.py

    def show_leaderboard(self):
        print("Leaderboard Clicked")

    def show_profile(self):
        print("Profile Clicked")

    def quit_game(self):
        pygame.mixer.music.stop()  # Stop music when quitting
        self.root.quit()

    def toggle_music(self):
        """Toggle music on and off."""
        if self.music_playing:
            pygame.mixer.music.pause()  # Pause the music
            self.music_button.config(text="Play Music")  # Change button text
        else:
            pygame.mixer.music.unpause()  # Unpause the music
            self.music_button.config(text="Mute Music")  # Change button text
        
        self.music_playing = not self.music_playing  # Toggle the state


if __name__ == "__main__":
    root = tk.Tk()
    game = BananaPuzzleGame(root)
    root.mainloop()


