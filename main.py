print("Learn your squares and cubes!")

##Open loop that will continue presenting powers tables for entered integers until the user wishes to quit
keepGoing = "y"
while keepGoing.lower() == "y":

    ##Prompt user to enter an integer
    userNumber = int(input ("Enter an integer: "))

    #Print heading for table
    print("Number   Squared     Cubed")
    print("======   =======     =====")
    for i in range(userNumber):
        i += 1
        print(str(i) + "          " + str(i**2) + "          " + str(i**3))
    keepGoing = input("Continue? (y/n)")
