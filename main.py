from art import text2art
from colorama import Fore

BELIEVE_AND_ACHEIVE= text2art("BELIEVE", font='block')+ text2art("AND", font='block')+ text2art("ACHEIVE", font='block')
hello_art= text2art("HELLO", font='sub-zero')
name=text2art("shouq")
print(Fore.MAGENTA+ BELIEVE_AND_ACHEIVE)
print(Fore.CYAN+hello_art)
print(Fore.YELLOW+name)