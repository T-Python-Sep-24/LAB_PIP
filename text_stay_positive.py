from art import text2art
from colorama import Fore, Style, init

init(autoreset=True)

stay_positive_art = text2art("STAY POSITIVE", font='rnd-small')
print(Fore.GREEN + Style.BRIGHT + stay_positive_art)
