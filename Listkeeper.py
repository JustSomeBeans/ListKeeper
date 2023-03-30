players = []

def add_player():
    players.append(input("Enter the player's name: "))
    print(f"{players[-1]} has been added to the list.\n")

def remove_player():
    name = input("Enter the player's name: ")
    if name.lower() in [p.lower() for p in players]:
        confirm = input(f"Are you sure you want to remove {name}? (y/n)\n")
        if confirm.lower() == "y":
            players.remove([p for p in players if p.lower() == name.lower()][0])
            print(f"{name} has been removed.\n")
        else:
            print(f"{name} was not removed.\n")
    else:
        print(f"{name} was not found.\n")

def next_player():
    if len(players) == 0:
        print("No players found.\n")
    else:
        print(f"It is {players[0]}'s turn.\n")
        players.append(players.pop(0))

def view_players():
    if len(players) == 0:
        print("No players found.\n")
    else:
        print("Current players in rotation:")
        print(*players, sep='\n')
        print()

def add_to_rotation():
    players.append(input("Enter the player's name: "))
    print(f"{players[-1]} has been added to the back of the rotation.\n")

def help_menu():
    print("1. Add player\n2. Remove player\n3. Next player\n4. View players\n5. Add player to rotation\n6. Help\n7. Quit\n")

print("Welcome to Listkeeper v2.1 by JustSomeBeans!\nTo get started enter the number corresponding to your selection\n")

while True:
    print("1. Add player\n2. Remove player\n3. Next player\n4. View players\n5. Add player to rotation\n6. Help\n7. Quit")
    choice = input("Enter your choice: ")
    if choice == "1": add_player()
    elif choice == "2": remove_player()
    elif choice == "3": next_player()
    elif choice == "4": view_players()
    elif choice == "5": add_to_rotation()
    elif choice == "6": help_menu()
    elif choice == "7":
        if input("Are you sure you want to quit? (y/n)\n").lower() == "y": break
        else: print("Program will continue.\n")
    else: print("Invalid choice. Please try again.\n")
