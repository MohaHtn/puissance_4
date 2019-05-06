# Projet AP1  : Puissance 1 - Journal

* **Auteur** : Mohamed Zidani

### Semaine du 25 au 31 mars : 
#### Objectifs
Prise en compte du sujet et réalisation de quelques fonctions.

Bilan : 
```python
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
            if case == 0:
                print('-', end='')
            elif case == 1:
                print('O', end='')
            elif case == 2:
                print('X', end='')
        print()
    print('=' * nc(grille))
    print(*[i for i in range(nc(grille))],sep='')
```
