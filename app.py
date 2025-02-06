from pywebio import start_server
from pywebio.input import input, NUMBER
from pywebio.output import put_image, put_text, put_buttons, clear
import requests

API_URL = "https://marcconrad.com/uob/banana/api.php"

def fetch_puzzle():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return None

def banana_puzzle():
    while True:
        clear()
        puzzle = fetch_puzzle()
        if not puzzle:
            put_text("Failed to load puzzle.")
            return

        put_text("Banana Puzzle Game 🍌")
        put_image(puzzle["question"])
        solution = puzzle["solution"]

        user_answer = input("Your answer:", type=NUMBER)
        if user_answer == solution:
            put_text("✅ Correct! 🎉")
        else:
            put_text("❌ Incorrect. Try again!")

        put_buttons(["Next Question"], onclick=lambda _: banana_puzzle())

if __name__ == "__main__":
    start_server(banana_puzzle, port=8080)
