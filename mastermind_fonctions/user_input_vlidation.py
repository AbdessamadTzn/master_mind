import sys
import os

# Add parent directory of the current script to system
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mastermind_fonctions import gen_combi_secrets
from mastermind_fonctions import player_interaction

# def user_input_verification():
def user_input_verification():

    combinaison = gen_combi_secrets.generation_combinaisons_secrets()
    print(combinaison)      #KEEP IT HERE FOR TESTING

    correctes = ['*']*4     #Pour remplacer les * par les chiffres bien placés

    num_chiffres_correctes = 0
    count = 0
    
    while count < 10:
        joueur_input = player_interaction.player_interaction()
        if combinaison == joueur_input:
            print("T'as trouvé la bonne combinaison!")
        else:
            for idx in range(0, 4):
                if (combinaison[idx] == joueur_input[idx]):
                    correctes[idx] = combinaison[idx] 
                    num_chiffres_correctes += 1
                    count += 1
                    print(f'Chiffres correctements devinés: {correctes}')
                    if count < 10:
                        print(f'T\'as encore {10 - count} chances!')
                    else:
                        print("Dommage, t'as pas deviné la bonne combinison !")
   
            



