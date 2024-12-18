import random 

def generation_combinaisons_secrets(level = 4, poss = 5) :
    
    secret_list = [ random.randint(1,5) for leng in range (level) ]
    return secret_list





