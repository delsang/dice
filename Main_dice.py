import sys
from dice_throw import dice_throw
from out_of_prison import out_of_prison
from free_or_prison import free_or_prison
from players import players

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

    while True:
        for i in range(len(names)):

            if i != len(names)-1:
                print(names[i], "It's your turn to play!\n")
                answer = free_or_prison().lower()
                if answer == 'y':
                    dice_throw()
                elif answer == 'quit':
                    exit()
                else :
                    out_of_prison()

            else:
                print(names[len(names)-1], "It's your turn to play!")
                answer = free_or_prison().lower()
                if answer == 'y':
                    dice_throw()
                elif answer == 'quit':
                    exit()
                else :
                    out_of_prison()

# Call to main function to run the program
if __name__ == "__main__":
    main()
