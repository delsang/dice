import random

def dice_throw():

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice5 = random.randint(1,6)
    dice6 = random.randint(1,6)

    input('*** Roll the dices... click enter! ***\n')

    print('The first dice is', dice1)
    print('The second dice is', dice2)
    print('Go ahead', dice1+dice2, 'steps \n')

    if dice1 == dice2:
        print('Lucky you! You get an other go! ')
        input('*** Roll the dices... click enter! ***\n')
        print('The new dices are', dice3, dice4, 'Go ahead', dice3 + dice4, 'steps\n')

    if dice1 == dice2 and dice3 == dice4:
        print('Lucky you! You get an other go! ')
        input('*** Roll the dices... click enter! ***\n')
        print('The new dices are', dice5, dice6, 'Go ahead', dice3 + dice4, 'steps\n')
    else:
        print ("That's it for now, time for the other player to play\n")

    if dice3 == dice4 and dice5 == dice6:
        print("Too much luck... Are you cheating? Go straight to prison\n")
