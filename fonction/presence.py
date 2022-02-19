from fonction.primitives import *
from fonction.liste.listefeuille import listefeuille

def questionPresent(question, monArbre):
    if estFeuille(monArbre):
        return False
    elif not estFeuille(monArbre):
        if question == monArbre[0]:
            return True
        else:
            return questionPresent(question, filsGauche(monArbre)) or questionPresent(question, filsDroit(monArbre))

def animalPresent(animal, monArbre):
    listeAnimal = listefeuille(monArbre)
    return animal in listeAnimal

