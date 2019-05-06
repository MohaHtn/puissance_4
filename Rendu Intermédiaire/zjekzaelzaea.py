# Puissance 4 : Mohamed Zidani

# 1 = rouge (joueur 1) O
# 2 = jaune (Joueur 2) X
# 0 = vide

from render_connect4 import *


def init_grille(nr, nc):
    """
    Initialise une grille de jeu de nr lignes et de nc colonnes, contenant aucun disque.
    :param nr: (int) nombre de lignes
    :param nc: (int) nombre de colonnes
    :return: (list) une grille de jeu.

    Examples :
    init_grille(2, 7):
    [[0, 0], [0, 0], [0, 0], [0, 0], [0,0] [0, 0], [0, 0]]

    init_grille(6, 7):
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    """
    return [[0 for i in range(nr)] for j in range(nc)]


def print_grille(grille):
    """
    Cette fonctione ne sert à rien, donc pas de documentation ! owo
    :param grille:
    :return:
    """
    for ligne in grille:
        string_ligne = ""
        for case in ligne:
            string_ligne += str(case)
        print(string_ligne)


def nr(grille):
    """
    Retourne le nombre de lignes de la grille.
    :param grille: (list) une grille
    :return: (int) le nombre de lignes de la grille
    """
    return len(grille)


def nc(grille):
    """
    Retourne le nombre de colonnes de la grille.
    :param grille: (list) une grille
    :return: (int) le nombre de colonnes de la grille
    """
    return len(grille[0])

def aff_grille(grille):
    """
    Affiche une grille avec des caractères.
    0 équivaut à rien, O (o majuscule) au joueur 1, X au joueur 2.
    :param grille: (list) une grille de jeu.
    :return: (none) Rien du tout.

    Exemples :
    aff_grille = [[1, 0, 1], [2, 0, 1], [1, 0, 0]]
    O-O
    X-O
    O--
    ===
    012

    aff_grille = [[1, 2, 2, 0, 1], [2, 1, 0, 2, 1], [1, 2, 0, 0, 0]]
    OXX-O
    X0-XO
    OX---
    =====
    01234
    """
    for ligne in grille:
        for case in ligne:
            if case == 0:                                   # astuce de proGamer : print("-OX"[case])
                print('-', end='')
            elif case == 1:
                print('O', end='')
            elif case == 2:
                print('X', end='')
        print()
    print('=' * nc(grille))
    print(*[i for i in range(nr(grille) +1)], sep='')           # si tu l'as oublié, go la rechercher.


def colonne_valide(c, grille):
    """
    Vérifie si la colonne c est un coup valide comparé à la grille g.
    :param c: (int) le numéro de la colonne.
    :param grille: (list) la grille de jeu.
    :return: (bool) Vrai ou Faux suivant si la colonne est valide ou pas.

    Exemples :
    colonne_valide(2, [[2,0,0,0],[1,0,0,2],[1,0,2,1]])
    True

    colonne_valide(2, [[0,0,1,0], [0,0,2,0], [0,0,1,0]])
    False
    """
    if c > len(grille) or c < 0:
        return False
    for i in range(nr(grille)):
        if grille[i][c] == 0:
            return True
    return False


def saisir_colonne_valide(grille):
    """
    Retient la valeur de la colonne si la colonne c d'une grille g est valide.
    :param grille: (list) La grille de jeu.
    :return: (int) la colonne en question.

    Exemples :
    colonne_valide(2, [[0, 0, 1, 0], [0, 0, 2, 0], [0, 0, 1, 0]])
    La colonne entrée n'est pas valide.

    colonne_valide(1, [[0, 0, 1, 0], [0, 0, 2, 0], [0, 0, 1, 0]])
    1
    """
    try:
        s = input('Saisir une colonne valide : ')
        if s == "exit":
            exit()
        cunt = int(s)
    except:
        print("La valeur entrée n'est pas un entier.")
        return saisir_colonne_valide(grille)
    if not colonne_valide(cunt, grille):
        print("La colonne entrée n'est pas valide.")
        return saisir_colonne_valide(grille)
    else:
        return cunt


def determiner_ligne(c, grille):
    """
    Détermine à quel ligne le jeton tombe, en fonction de la colonne c de la grille.
    :param c: (int) la colonne
    :param grille: (list) La grille de jeu
    :return: (int) la ligne ou le jeton tombe.

    Exemples :
    determiner_ligne(2, [[0, 0, 1, 0], [0, 0, 2, 0], [0, 0, 1, 0]])
    -1

    determiner_ligne(1, [[0, 0, 1, 0], [0, 0, 2, 0], [0, 0, 1, 0]])
    2
    """
    for i in range(nr(grille)):
        if grille[i][c] != 0:
            return i - 1
    return len(grille) - 1


def modif_grille(grille, p, c):
    """
    Modifie la grille avec le jeton p, dans la colonne c, dans la grille g.
    :param grille: (list) La grille de jeu.
    :param p: (int) Le joueur : 1 pour le Joueur 1, 2, pour le Joueur 2.
    :param c: (int) la colonne de la grille.
    :return: (none) Rien du tout.
    """
    grille[determiner_ligne(c, grille)][c] = p


def is_in_range(grille, r, c):
    """
    Vérifie si la grille 
    :param grille:
    :param r:
    :param c:
    :return:
    """
    if nr(grille) < r and nc(grille) < c and r < 0 and c < 0:
        return True
    else:
        return False


def is_align4(grille, lc, p):
    lc = filter(lambda coord: is_in_range(grille, coord[0], coord[1]), lc)
    nbConsecutif = 0
    last = 0
    for coord in lc:
        contenu = grille[coord[0]][coord[1]]
        if (contenu == last and contenu == p):
            nbConsecutif += 1
        else:
            nbConsecutif = 0
        last = contenu
        if nbConsecutif == 4:
            print('eizajekzaleza')
            return True
    return False


def play():
    p = 1
    tour = 1
    game_over= False
    grille = init_grille(6, 7)

    while not game_over:
        draw_connect4(grille)
        c = saisir_colonne_valide(grille)
        r = determiner_ligne(c, grille)
        modif_grille(grille, p, c)
        if tour % 2 == 0:
            p = 1
        else:
            p = 2
        print("Au tour du Joueur " + str(p) + " !" + '\n' + "Tour " + str(tour))
        lc1 = [(r, c - 3), (r, c - 2), (r, c - 1), (r, c), (r, c + 1), (r, c + 2), (r, c + 3)]
        lc2 = [(r - 3, c - 3), (r - 2, c - 2), (r - 1, c - 1), (r, c),(r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)]
        lc3 = [(r - 3, c), (r - 2, c), (r - 1, c), (r, c), (r + 1, c), (r + 2, c), (r + 3, c)]
        lc4 = [(r - 3, c + 3), (r - 2, c + 2), (r - 1, c + 1), (r, c),(r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)]
        is_align4(grille, lc1, p)
        print('lc1 vraie')
        is_align4(grille, lc2, p)
        print('lc2 vraie')
        is_align4(grille, lc3, p)
        print('lc3 vraie')
        is_align4(grille, lc4, p)
        print('lc4 vraie')
        nbFull = 0
        tour += 1
        for line in grille:
            if not 0 in line:
                nbFull += 1
        game_over = (nbFull == len(grille))
    print('Jeu terminé !')

# def is_win(grille, r, c, p):


if __name__ == "__main__":
    init_draw(w=450, h=480)
    play()
    wait_quit()