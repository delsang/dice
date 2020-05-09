import sys
from dice_throw import dice_throw
from out_of_prison import out_of_prison
from free_or_prison import free_or_prison
from players import players
from jail import injail

def main():

    names = players()

    # Welcome text with all participants type_names

    print('\nNice to meet you', end ="")
    for i in range(len(names)):
        if i != len(names)-1:
            print(',', names[i], end ="")
        else:
            print(' and', names[len(names)-1], end ="")
    print(", let's start playing!\n")

    #at the start, everyone is free
    register = {}
    jail_start = False

    for i in range(len(names)):
        register[names[i]] = jail_start

    
    while True:
        for i in range(len(names)):

            print(names[i], "It's your turn to play!\n")

            # throw the dice if the player is out of jail and saves the result
            if register[names[i]] == False :
                jail = dice_throw()
                register[names[i]] = jail

                #asks if the player has ended up in jail and saves the result
                if register[names[i]] == False :
                    jail = injail()
                    register[names[i]] = jail

            #throw the dice if the player is in jail and saves the result
            else :
                jail = out_of_prison()
                register[names[i]] = jail




# Call to main function to run the program
if __name__ == "__main__":
    main()
