def joueur_interaction():

    try:
        combinaison_joueur = int(input("Entrer une combinaison de 4 nombres entiers: "))
    
        if len(str(combinaison_joueur)) != 4:

            print("Tu dois entrer exactement 4 nombres !")
            return joueur_interaction() #To keep calling function using recursio & do not exit

        combinaison_joueur = [int(num) for num in str(combinaison_joueur)]

        return combinaison_joueur

    except ValueError:
        #Catch error if input is not digit !
        print("Erreur: la combinaison doit etre composée des entiers valide")

    



