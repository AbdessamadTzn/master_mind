def player_interaction():

    accepted_digits = [0, 1, 2, 3, 4, 5]

    try:
        player_combination = int(input("Enter a combination of 4 integers between 0 and 5: "))
    
        if len(str(player_combination)) != 4:

            print("You must enter exactly 4 numbers!")
            return joueur_interaction()     #To keep calling function using recursion logic & do not exit

        for x in str(player_combination):
            if int(x) not in accepted_digits:
                print("You must enter digits between 0 and 5!")
                return player_interaction()     



        player_combination = [int(num) for num in str(player_combination)]

        return player_combination

    except ValueError:
        #Catch error if input is not digit !
        print("The combination must consist of valid integers!")
        return player_interaction()
