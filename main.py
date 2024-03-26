from termcolor import colored, cprint
from random import randint
from lib.handleMessage import handleError

# Init
T = 0
list = [0, 0, 0, 0]
init = 0
display = [
    "Choose the min number : ",
    "Choose the max number : ",
    "Choose the nb of tries : "
]

errPointer = 0

while init < 3:
    try:
        # 
        list[init] = int(input(display[init]))

        # Max number
        if init == 1 and list[1] <= list[0]:
            raise ValueError("Merci de mettre un chiffre plus grand", errPointer)

        # Try number
        if init == 2 and list[init] == 0:
            raise ValueError("Ho le petit comique", errPointer)
        
        init+=1
    except ValueError as err:
        errPointer = handleError(err.args, errPointer)


# ---------------------------------------------------
        
print("The min is {}, the max is {}, you have {} tries".format(list[0], list[1], list[2]))

# ---------------------------------------------------

# Get random number
list[3] = randint(list[0], list[1])

# Main game
nbTry=1
while nbTry <= list[2] and T != list[3]:
    print("START MAIN GAME")

    try:
        T = int(input())

        # Test
        if T < list[0] or T > list[1]:            
            raise ValueError("Merci de respecter les bornes min et max", "hjk")
        
        nbTry+=1        
    except ValueError as err:
        errPointer = handleError(err.args, errPointer)

# Result
if T == list[3]:
    cprint('Year you did it !', "green")
else:
    cprint("Nice try but please turn on your brain !", "red")
