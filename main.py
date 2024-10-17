from art import *
from colorama import Fore, Back

# block font text art
blockTxt = text2art('''BELIEVE
AND
ACHEIVE''', font='block')
print(blockTxt)

# sub-zero font text art
sub0Txt = text2art("HELLO", font='sub_zero')
print(sub0Txt)

#------Bonus------

# random font text art
randomTxt = text2art("Ghaliah", font='rand')
print(randomTxt)

# random font text art
multiline = text2art('''Hello World..
This is Ghaliah
''', font='small')
print(multiline)

# Coloring some text
print(Fore.CYAN + multiline)
print(Back.MAGENTA + randomTxt)
print(Back.RESET + sub0Txt)
