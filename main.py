from art import *
from pyfiglet import *
from colorama import Back

ArtF = figlet_format("BELIEVE AND ACHIEVE", font="block") 
print(Back.BLUE + 'BELIEVE AND ACHEIVE:>>')
print(ArtF, '\n')

ArtA = text2art("HELLO",font='sub-zero',chr_ignore=True) 
print(Back.LIGHTBLACK_EX + 'HELLO:>>')
print(ArtA, '\n')

