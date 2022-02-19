from fonction.primitives import *

def listefeuille(monArbre, liste=[]):
    if estFeuille(monArbre):
        return [monArbre]

    return listefeuille(filsGauche(monArbre), liste) + listefeuille(filsDroit(monArbre), liste)


