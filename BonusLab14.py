#Bonus Lab 14

from art import *
from colorama import Fore, Back, Style, init

init()

text1 = text2art("Hi All", font="rnd-xlarge", chr_ignore=True)
print(Fore.BLUE + Back.BLACK + text1 + Style.RESET_ALL)

text2 = text2art("Bye", font="rnd-xlarge")
print(Fore.RED + text2 + Style.RESET_ALL)

text3 = text2art("HI", "xlarge")
print(Fore.CYAN + Back.WHITE + text3 + Style.RESET_ALL)

buble_text = text2art("Khulood", font="block", chr_ignore=True)
print(Fore.LIGHTWHITE_EX + buble_text + Style.RESET_ALL)

buble_text2 = text2art("GH", chr_ignore=True)
print(Fore.LIGHTYELLOW_EX + buble_text2 + Style.RESET_ALL)
