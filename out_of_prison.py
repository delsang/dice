import random

def out_of_prison():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice5 = random.randint(1,6)
    dice6 = random.randint(1,6)

    input("*** Let's get you out of there, roll the dices, click enter! ***\n")

    if dice1 == dice2:
        print(dice1, dice2,'yay! you are out!\n')
    else:
        print('You draw', dice1, dice2)
        input('2 more chances, try again!\n')

        if dice1 != dice2 and dice3 == dice4:
            print(dice3, dice4, 'yay! you are out!\n')
        else :
            print('You draw', dice3, dice4)
            input('1 more chance, try again!\n')

            if dice1 != dice2 and dice3 != dice4 and dice5 == dice6:
                print(dice5, dice6, 'That was close but you made it! you are out!\n')
            else:
                print('You draw', dice5, dice6, '\nSorry darling, you stay in!\n')
