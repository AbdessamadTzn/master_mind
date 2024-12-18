import sys
import os




# Add parent directory of the current script to system
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mastermind_fonctions import gen_combi_secrets
from mastermind_fonctions import joueur_interaction

# def user_input_verification():
if __name__ == '__main__':
    combinaison = gen_combi_secrets.generation_combinaisons_secrets()
    print(combinaison)
    joueur_input = joueur_interaction.joueur_interaction()

    if combinaison == joueur_input:
        print("T'as trouvé la bonne combinaison!")
    else:
        correctes = ['*']*4     #Pour remplacer les * par les chiffres bien placés
        combinaison = str(combinaison)
        joueur_input = str(joueur_input)
        num_chiffres_correctes = 0

        for num in range(0, 4):
            if (combinaison[num] == joueur_input[num]):
                correctes[num] == joueur_input[num]
                num_chiffres_correctes += 1
            else:
                continue
        
        if num_chiffres_correctes < 4 :
            print(f'C\'est pas la bonne combinaison, mais t\'as deviné {num_chiffres_correctes} corrctements')
            print(f'Chiffres correctements devinés: {correctes}')
        else:
            print("Dommage, t'as pas deviné la bonne combinison !")
            



