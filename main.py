from art import text2art
from colorama import Fore
phrases = {
    "BELIEVE AND ACHIEVE": "block",
    "HELLO": "sub-zero",
    "MOHAMMED":"bubble"
}
for phrase, font in phrases.items():
    art_text = text2art(phrase,font=font)
    print(Fore.BLUE + art_text)