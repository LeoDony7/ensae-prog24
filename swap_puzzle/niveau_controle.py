
import itertools
import random

from swap_puzzle.A_star import Node
from swap_puzzle.A_star import h




def game_level(level) :
    assert level in ('easy', 'intermediate', 'hard', 'impossible')
    
    
    liste_grilles = [] 
    for n in range (10): # On choisit arbitrairement de ne pas dépasser les matrices de 10 lignes
        for m in range (10): # et les 10 colonnes
            bonne_liste=[i for i in range(1,(n*m)+1)] #Ici on crée la liste ordonnée des entiers de 1 à nm
            liste_permutations=itertools.permutations(bonne_liste) # à partir de laquelle on crée toutes les permutations possibles
    
            for M in liste_permutations : #On met maintenant les listes sous forme de matrice de taille n,m
                M_grille = [ [0 for j in range (m)] for i in range (n)]
                for i in range (n):
                    for j in range (m):
                        M_grille[i][j]=M[i+j]
        
                liste_grilles.append(Node(M_grille, h(M_grille))) # Enfin on ajoute chaque matrice à notre liste contenant toutes les grilles
    
    #On initialise ensuite des listes vides de niveau dans lesquelles on rangera les grilles
    #selon le niveau de difficulté estimé
    liste_easy = []
    liste_intermediate = []
    liste_hard = []
    liste_impossible = []
    
    for M in liste_grilles :
        if len(M) < 4 and len(M[0]) < 5 :
            liste_easy.append(M) # Toute liste de taille infèrieure à 4x5 est considérée facile
        
        elif (len(M) < 8 and len(M[0]) < 9) or (len(M) < 4 and len(M) > 4) :
            if h(M) < 8*9/4 : # L'heuristique maximale possible est 8*9/2 (i.e aucune case d'une grille 8x9 à sa place), on découpe en deux sachant cela
                liste_intermediate.append(M) # Une grille d'heuristique dans la première moitié est classée dans le niveau intermédiaire
            else :
                liste_hard.append(M) # Une grille d'heuristique dans la deuxième moitié est considérée difficile
    
        else : #Toutes autre grille plus grande
            if h(M)<11 :
                liste_intermediate.append(M) # est considérée de niveau intermédiaire si peut nécessiter moins de 10 swaps pour être résolue
            if h(M)< 40 and h>10 :
                liste_hard.append(M) # difficle si d'heuristique entre 11 et 4O
            else :
                liste_impossible.append(M) # IMPOSSIBLE sinon

    # Enfin on renvoie une liste aléatoire de la liste correspondant au niveau demandé
    
    if level == 'easy' :
        return random(liste_easy)
    
    if level == 'intermediate' :
        return random(liste_intermediate)
    
    if level == 'hard' :
        return random(liste_hard)
    
    if level == 'impossible' :
        return random(liste_impossible)
    
    return None