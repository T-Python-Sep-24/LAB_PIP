from art import *  
from colorama import Fore , Style

print(text2art("BELIEVE \n  AND \n ACHIEVE", font='block'))
print(text2art("HELLO", font='sub-zero'))



#Bonus

Sentences = [
   
    ("harry potter", "banner"),
    ("winter is coming.", "random"),
    ("destiny is all.", "slant")
]


for Sentences ,font in Sentences:

    art_Sentences =text2art(Sentences,font)
    colored_Sentences = f"{Fore.CYAN}{art_Sentences}{Style.RESET_ALL}"
    print(colored_Sentences)







