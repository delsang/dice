import sys
from dice_throw import dice_throw
from out_of_prison import out_of_prison
from free_or_prison import free_or_prison

def main():

    while True:
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
