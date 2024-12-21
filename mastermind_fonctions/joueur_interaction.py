def joueur_interaction():

    chiffres_acceptes = [0, 1, 2, 3, 4, 5]

    try:
        combinaison_joueur = int(input("Entrer une combinaison de 4 nombres entiers entre 0 et 5: "))
    
        if len(str(combinaison_joueur)) != 4:

            print("Tu dois entrer exactement 4 nombres !")
            return joueur_interaction()     #To keep calling function using recursio & do not exit

        for x in str(combinaison_joueur):
            if int(x) not in chiffres_acceptes:
                print("Tu dois entrer des chiffres compris entre 0 et 5 !")
                return joueur_interaction()     



        combinaison_joueur = [int(num) for num in str(combinaison_joueur)]

        return combinaison_joueur

    except ValueError:
        #Catch error if input is not digit !
        print("La combinaison doit etre composée des entiers valide")
        return joueur_interaction()
