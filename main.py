from art import text2art
from colorama import Back,Fore


b = text2art("BELIEVE AND ACHIEVE", font="block")
print(Fore.BLUE + b)

hello = text2art( "HELLO", font="sub-zero")
print(Back.GREEN + hello)

text = text2art( "testing art", font="bulbhead")
print(Back.YELLOW + text)