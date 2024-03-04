
import itertools
import random

from swap_puzzle.A_star_copy import Nodee
from swap_puzzle.A_star_copy import h




def game_level(level) :
    assert level in ('easy', 'intermediate', 'hard', 'impossible')
    
    #(n,m) = tuple_size
    #assert n < 10
    #assert m < 10
    liste_grilles = []
    for n in range (10):
        for m in range (10): 
            bonne_liste=[i for i in range(1,(n*m)+1)]
            liste_permutations=itertools.permutations(bonne_liste)
    
            for M in liste_permutations :
                M_grille = [ [0 for j in range (m)] for i in range (n)]
                for i in range (n):
                    for j in range (m):
                        M_grille[i][j]=M[i+j]
        
                liste_grilles.append(Nodee(M_grille, h(M_grille)))
    
    liste_easy = []
    liste_intermediate = []
    liste_hard = []
    liste_impossible = []


    for M in liste_grilles :
        if len(M) < 4 and len(M[0]) < 5 :
            liste_easy.append(M)
        
        elif (len(M) < 8 and len(M[0]) < 9) or (len(M) < 4 and len(M) > 4) :
            if h(M) < 8*9/2 :
                liste_intermediate.append(M)
            else :
                liste_hard.append(M) 
    
        else :
            if h(M)<11 :
                liste_intermediate.append(M)
            if h(M)< 40 :
                liste_hard.append(M)
            else :
                liste_impossible.append(M)

    
    if level == 'easy' :
        return random(liste_easy)
    
    if level == 'intermediate' :
        return random(liste_intermediate)
    
    if level == 'hard' :
        return random(liste_hard)
    
    if level == 'impossible' :
        return random(liste_impossible)



