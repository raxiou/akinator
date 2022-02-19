def creerArbre(racine, gauche, droit):
    return [racine, gauche, droit]


def estFeuille(arbre):
    return type(arbre) is str


def racine(arbre):
    return arbre[1] != [] or arbre[2] != []


def filsGaucheExiste(arbre):
    return arbre[1] != []


def filsDroitExiste(arbre):
    return arbre[2] != []


def filsGauche(arbre):
    return arbre[1]


def filsDroit(arbre):
    return arbre[2]