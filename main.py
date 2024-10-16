from art import *
from colorama import Fore,Back,Style

art_1 =text2art("HELLO",font="sub-zero")
art_2 =text2art("BELIEVE\nAND\nACHEIVE\n",font="block") 
art_4=decor('diamond1')
art_3=text2art("shooting\nfor\nthe\nmoon\nbut\nthe\nstars\njust\nfine",font="alligator")
print(Fore.LIGHTBLUE_EX+art_2)
print(Style.DIM+Fore.CYAN+art_1)
print(Fore.CYAN+Style.BRIGHT+ art_4*21)
print(Fore.LIGHTRED_EX+Style.DIM+art_3)
print(Fore.CYAN+Style.BRIGHT+ art_4*21)



