# makes an empty list to hold players
players = []

# defines the function to add a player to the list
def add_player():
    # prompts user for player name
    name = input("Enter the player's name: ")
    # adds player to the list
    players.append(name)
    # prints response message
    print(f"{name} has been added to the list.\n")

# defines the function to remove a player from the list
def remove_player():
    # prompts user for the player's name
    name = input("Enter the player's name: ")
    # checks if player is in the list
    if name.lower() in [p.lower() for p in players]:
        # asks user before removing player
        confirm = input(f"Are you sure you want to remove {name}? (y/n)\n")
        if confirm.lower() == "y":
            # removes player from the list
            players.remove([p for p in players if p.lower() == name.lower()][0])
            # prints response message
            print(f"{name} has been removed.\n")
        else:
            # prints message confirming the player was not removed
            print(f"{name} was not removed.\n")
    else:
        # prints message if player isn't not found in the list
        print(f"{name} was not found.\n")

# defines the function to go to the next player in the list
def next_player():
    # checks if there are any players in the list
    if len(players) == 0:
        # prints message if there are no players
        print("No players found.\n")
    else:
        # prints message showing whose turn it is
        print(f"It is {players[0]}'s turn.\n")
        # moves the first player to the end of the list
        players.append(players.pop(0))

# defines function to display the current list of players
def view_players():
    # checks if there are any players in the list
    if len(players) == 0:
        # prints response message if there are no players in the list
        print("No players found.\n")
    else:
        # prints the list of players
        print("Current players in rotation:")
        for player in players:
            print(player)
        print("\n")
# defines the function to add a player to the back of the rotation
def add_to_rotation():
    # prompts user for player name
    name = input("Enter the player's name: ")
    # adds player to the back of the list
    players.append(name)
    # print response message
    print(f"{name} has been added to the back of the rotation.\n")

# defines the function to display the help menu
def help_menu():
    # prints a list of available options
    print("1. Add player - Adds a new player to the list")
    print("2. Remove player - Removes a player from the list")
    print("3. Next player - Advances to the next player in the rotation")
    print("4. View players - Shows the list of players currently in rotation")
    print("5. Add player to rotation - Adds a new player to the back of the rotation")
    print("6. Help - Displays this help menu")
    print("7. Quit - Exits the program\n")

print("Welcome to Listkeeper 2.0 by JustSomeBeans!\nTo get started enter the number corripsonding to your selection\n")

# main program loop
while True:
    # displays the main menu
    print("1. Add player")
    print("2. Remove player")
    print("3. Next player")
    print("4. View players")
    print("5. Add player to rotation")
    print("6. Help")
    print("7. Quit")
    # prompts the user for choice
    choice = input("Enter your choice: ")
    # calls defined function based on user choice
    if choice == "1":
        add_player()
    elif choice == "2":
        remove_player()
    elif choice == "3":
        next_player()
    elif choice == "4":
        view_players()
    elif choice == "5":
        add_to_rotation()
    elif choice == "6":
        help_menu()
    elif choice == "7":
        # asks user if they really want to quit
        confirm = input("Are you sure you want to quit? (y/n)\n")
        # quits program
        if confirm.lower() == "y":
            break
        else:
            print("Program will continue.\n")
    # tells user if their input was invalid
    else:
        print("Invalid choice. Please try again.\n")
