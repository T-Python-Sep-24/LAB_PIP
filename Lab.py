from art import text2art
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define a list of phrases and fonts
phrases = [
    ("Hessa Almasaad", "block"),
    ("Full Stack Developer", "slant"),
    ("Dream Big, Work Hard", "random"),
    ("Python is flixelble language ", "tubular"),
    ("Tuwaiq Academy", "starwars"),
    ("Keep Pushing Forward", "fuzzy"),
    ("Gaming is my hobby", "doom"),
    ("Favorite American television is FRIENDS", "banner"),
]

# Define a list of colors
colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.CYAN,
    Fore.MAGENTA,
    Fore.WHITE,
]

# Loop through each phrase, create art, and print it in color
for phrase, font in phrases:
    # Get a random color from the colors list
    color = colors[hash(phrase) % len(colors)]  # Hash to ensure different colors for different phrases
    # Create the art and print it
    art_text = text2art(phrase, font=font)
    print(color + art_text + Style.RESET_ALL)


