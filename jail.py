from players import players
# at the end of the turn, ask if the person is in jail of not and store the value
# in the register dictionnary

def injail():

    print('Did you end up in Jail? Y or N')
    answer = input('')

    if answer == 'Y' or answer == 'y':
        jail = True
    else:
        jail = False

    return(jail)
