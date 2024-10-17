from art import text2art  
from colorama import Fore, Style, init  

# Initialize colorama
init(autoreset=True)

font_block= text2art("BELIEVE AND ACHIEVE", font='block')
print(font_block)

# Printing "HELLO" in sub-zero font
font_zero= text2art("HELLO", font='sub-zero')
print(font_zero)

# Bonus: 
# Phrase 1: 
phrase1 = text2art("DREAM BIG", font='block')
print(Fore.YELLOW + phrase1 + Style.RESET_ALL)

# Phrase 2: 
phrase2 = text2art("STAY POSITIVE", font='random')
print(Fore.MAGENTA + phrase2 + Style.RESET_ALL)

# Phrase 3:
phrase3 = text2art("NEVER GIVE UP", font='slant')
print(Fore.RED + phrase3 + Style.RESET_ALL)
