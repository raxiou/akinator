from fonction.primitives import *
def nbNoeud(monArbre):
    if estFeuille(monArbre):
        return 1

    return 1 + nbNoeud(filsGauche(monArbre)) + nbNoeud(filsDroit(monArbre))


def nbFeuille(monArbre):
    if estFeuille(monArbre):
        return 1

    return 0 + nbFeuille(filsGauche(monArbre)) + nbFeuille(filsDroit(monArbre))
