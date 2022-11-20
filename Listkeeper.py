print("Welcome to list keeper by JustSomeBeans!\ntype /help for a list of commands\n")
order = 1 #setting global variables
count = 1
turn = 1
lit = []
verify = 0 
def inpt(): #console checking function
    global order, lit, inp, turn, count, verify #declaring global variables
    bypass = 0 #way of bypassing bullshit code order idk if i need this left it in anyway
    inp = str(input("\n")) #gets user command input
    if inp[0:5] == "/help": #detects /help in inp string
        print("/add [username] - adds a user to the rotation\n/new [username] - adds a new player to the rototation behind the player's who turn it is\n/next - tells you which user is next\n/order - gives you the rotation order\n/remove [username] - removes a user from the rotation")
        #line above listing the available commands
    if inp[0:5] == "/add ": #detects /add in inp string
        if verify == 0:
            lit.append(inp.replace("/add ", "")) #adds the new user to the list at the end
            count = len(lit) #updates the player count
            print("Added " + inp.replace("/add ", "")) #console response
            print("Total playe(s) is now: " + str(count)) #console response
        if verify != 0:
            yn1 = str(input("Using /add will add " + inp.replace("/add", "") + "to the bottom of the list instead of behind the current player causing them to cut the line\nUsing /add after rotation has started may cause listing error\nAre you sure you want to use /add instead of /new? (y/n)"))
            if yn1[0] == "y":
                lit.append(inp.replace("/add ", "")) #adds the new user to the list at the end
                count = len(lit) #updates the player count
                print("Added " + inp.replace("/add ", "")) #console response
                print("Total playe(s) is now: " + str(count)) #console response
            if yn1[0] == "n":
                print("aborted adding " + inp.replace("/add", ""))
    if inp[0:5] == "/new ": #detects /new in inp string
        lit.insert((turn - 2), inp.replace("/new ", "")) #inserts the new player into the position behind the player's who turn it is
        count = len(lit) #updates player count
        print("Added " + inp.replace("/new ", "")) #console response
        print("Total playe(s) is now: " + str(count)) #console response
        if turn != count: #preserving who's turn it is
            turn = turn + 1 #updating the turn if the roation is not at the end
        elif turn == count:
            turn = 1 #updating the turn if the rotation is at the end
        
    if inp[0:5] == "/next": #detects /next
        if turn == count: #makes sure the turn order loops when it gets to the end of the list
            print("it is " + lit[(turn - 1)] + "'s turn\n") #console response
            turn = 1 #loops turn to start of the list
            bypass = 1 #enables the bypass of the next logic statement
        elif turn != count and bypass == 0: #prints who's turn it is and updates who's next
            print("It is " + lit[(turn - 1)] + "'s turn\n") #console repsonse
            turn = turn + 1 #updates turn
        bypass = 0
        verify = 1

    if inp[0:8] == "/remove ":
        yn = str(input("Are you sure you want to remove " + inp.replace("/remove ", "") + "? | (y/n)\n"))
        if yn[0] == "y":
            lit.remove(inp.replace("/remove ", "")) #removes player frrom the list
            count = count - 1 #updates count
            turn = turn - 1 #preserves turn order
            print("Removed " + inp.replace("/remove", "")) #console response
            print("Total player(s) is now " + str(count)) #console response
        if yn[0] == "n":
            print("Aborted removal of " + inp.replace("/remove ", ""))

    if inp[0:6] == "/order": #detects /order command
        print(lit) #console response
    inpt()
inpt()
