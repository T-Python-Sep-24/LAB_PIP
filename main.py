from art import text2art
from colorama import Fore, Style, init

# initializes the colorama module for use
init()

# print using the "block" font in red color
text_block = text2art("BELIEVE AND ACHIEVE", font='block')
print(Fore.RED + text_block + Style.RESET_ALL)

# print using the "sub-zero" font in blue color
text_sub_zero = text2art("HELLO", font='sub-zero')
print(Fore.BLUE + text_sub_zero + Style.RESET_ALL)

text_success = text2art("SUCCESS", font='block')
print(Fore.GREEN + text_success + Style.RESET_ALL)