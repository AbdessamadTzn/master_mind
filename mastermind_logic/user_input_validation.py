import sys
import os

# Add parent directory of the current script to system
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mastermind_logic import gen_combi_secrets
from mastermind_logic import player_interaction

def user_input_verification():

    combination = gen_combi_secrets.generate_secret_combinations()
    print(combination)      #KEEP IT HERE FOR TESTING

    corrects = ['*']*4     #To replace the * with the correctly placed digits

    num_correct_digits = 0
    count = 0
    
    while count < 10:
        user_input, count = player_interaction.player_interaction(count)
        if combination == user_input:
            print("You guessed the right combination!")
            return
        else:
            for idx in range(0, 4):
                if (combination[idx] == user_input[idx]):
                    corrects[idx] = combination[idx] 
                    num_correct_digits += 1
            
            if count < 10:
                print(f'Correctly guessed digits: {corrects}')
                print(f'You have {10 - count} chances left!')
            else:
                print("Game Over!, you didn't guess the correct combination!")
                print(f'The correct combination was: {combination}')
                return
        
        
            



