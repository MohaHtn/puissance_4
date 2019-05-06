def play():
    p = 1
    tour = 1
    game_over= False
    grille = init_grille(6, 7)

    while not game_over:
        print('Tour', tour)
        draw_connect4(grille)
        c = saisir_colonne_valide(grille)
        r = determiner_ligne(c, grille)
        lc1 = [(r, c - 3), (r, c - 2), (r, c - 1), (r, c), (r, c + 1), (r, c + 2), (r, c + 3)]
        lc2 = [(r - 3, c - 3), (r - 2, c - 2), (r - 1, c - 1), (r, c), (r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)]
        lc3 = [(r - 3, c), (r - 2, c), (r - 1, c), (r, c), (r + 1, c), (r + 2, c), (r + 3, c)]
        lc4 = [(r - 3, c + 3), (r - 2, c + 2), (r - 1, c + 1), (r, c), (r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)]
        is_align4(grille, lc1, p)
        is_align4(grille, lc2, p)
        is_align4(grille, lc3, p)
        is_align4(grille, lc4, p)
        modif_grille(grille, p, c)
        if tour % 2 == 0:
            p = 1
        else:
            p = 2
        print("Au tour du Joueur " + str(p) + " !")
        nbFull = 0
        if p == 2:
            tour += 1
        for line in grille:
            if not 0 in line:
                nbFull += 1
        game_over = (nbFull == len(grille))
    print('Jeu terminé !')