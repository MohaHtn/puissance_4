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

determiner_ligne(2, [[0, 0, 1, 0], [0, 0, 2, 0], [0, 0, 1, 0]])
