def players():
    # get names for each players
    names = []
    print("\n*** Welcome to the Dice!***\n")
    type_names = input("\nWrite down each player's name, separated by a comma :\n")
    players_names = [ x.strip() for x in type_names.split(',') ]

    # get the names in an array
    for players_name in players_names:
        names.append(players_name)


    return names
