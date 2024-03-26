from termcolor import colored, cprint
errMessage = [
    "Par contre fait gaffe quand même",
    "C'est pas possible tu le fais exprès",
    "Viviblement tu ne sais pas te servir d'un clavier",
    "Essaye avec l'autre main des fois que !",
    "Visiblement l'informatique est toi ça fait 2, on va pas aller plus loin"
]


def handleError(messages, pointer):
    if len(messages) == 2:
        cprint(messages[0], 'red')
    else:
        cprint("Please write a real number", "red")

    pointer+=1
    if pointer > 2:
        cprint(errMessage[pointer-3], "yellow")

    if pointer == 7:
        raise SystemExit
    
    return pointer
