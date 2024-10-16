from colorama import Fore, Back, Style
from art import *

myText = text2art("BELIEVE AND ACHIEVE",font='block')
print(myText)
print(Fore.RED)
tprint("BELIEVE AND ACHIEVE")
myText2 = text2art("HELLO",font='sub-zero')
print(myText2)

print(Fore.YELLOW + Back.BLACK)
tprint("I Will Make Them Notice Me\n Without making noises", font='big ')

print(Style.BRIGHT + Back.CYAN + Fore.RED + "HMZH DABBAH")
print(Back.RESET)
print(Fore.RESET)


print(Fore.YELLOW)

