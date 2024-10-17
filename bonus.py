from colorama import Fore,Back
from art import *


ph1=text2art("SUCCESS\nJOURNEY", font="slant")
print(Fore.GREEN)
print(ph1)
ph2=text2art("DREAM\nBIG", font="isometric1")
print(Fore.RESET)
print(Fore.MAGENTA)
print(Back.BLACK)
print(ph2)
ph3=text2art("      STAY\nPOSITIVE", font="rectangles")
print(Fore.RESET)
print(Back.CYAN)
print(ph3)



