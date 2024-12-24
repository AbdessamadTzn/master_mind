def player_interaction(count):

    accepted_digits = [0, 1, 2, 3, 4, 5]

    while True:
        try:
            player_combination = input("Enter a combination of 4 integers between 0 and 5: ")
            count += 1
        
            if len(str(player_combination)) != 4:
                print("You must enter exactly 4 numbers!")
                print(f'You have {10 - count} chances left!')
                return player_interaction(count)     #To keep calling function using recursion logic & do not exit

            for x in str(player_combination):
                if int(x) not in accepted_digits:
                    print("You must enter digits between 0 and 5!")
                    print(f'You have {10 - count} chances left!')
                    return player_interaction(count)    

            player_combination = [int(num) for num in str(player_combination)]
            return player_combination, count

        except ValueError:
            #Catch error if input is not digit !
            print("The combination must consist of valid integers!")
            print(f'You have {10 - count} chances left!')
            return player_interaction(count)
