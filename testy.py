# Puissance 4 : Mohamed Zidani

# 1 = rouge (joueur 1) O
# 2 = jaune (Joueur 2) X
# 0 = vide

def init_grille(nr, nc):
    return [[0 for i in range(nr)] for j in range(nc)]


def print_grille(grille):
    for ligne in grille:
        string_ligne = ""
        for case in ligne:
            string_ligne += str(case)
        print(string_ligne)

def nr(grille):
    return len(grille)

def nc(grille):
    return len(grille[0])

def aff_grille(grille):
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
    print(*[i for i in range(nr(grille))],sep='')           # si tu l'as oublié, go la rechercher.


def colonne_valide(c, grille):
    if c > len(grille) or c < 0:
        return False
    for i in range(nr(grille)):
        if grille[i][c] == 0:
            return True
    return False

def saisir_colonne_valide(grille):
    try:
        cunt = int(input('Saisir une colonne valide : '))
    except:
        print ('t con ou koi')
        saisir_colonne_valide(grille)
        return
    if colonne_valide(cunt, grille) == False:
        print('c pa valid')
        saisir_colonne_valide(grille)
    else:
        return cunt

def determiner_ligne(c, grille):
    for i in range(nr(grille)):
        if grille[i][c] == 1 or 2:
            return i - 1
    return len(grille) - 1

def modif_grille(grille, p, c):
    grille[determiner_ligne(c, grille)][c] = p

def play():
    p = 1
    tour = 0
    game_over= False
    grille = init_grille(6, 7)

    while not game_over:
        c = saisir_colonne_valide(grille)
        determiner_ligne(c, grille)
        modif_grille(grille, p, c)
        tour += 1
        if tour % 2 == 0:
            print("Au tour du joueur 1 ! pd")
            p = 1
        else:
            print("toi tg")
            p = 2




if __name__=="__main__":
    p = 1
    tour = 0
    grille = init_grille(6, 7)

    # Joueur 1
    saisir_colonne_valide(grille)
