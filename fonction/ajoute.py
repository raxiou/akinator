from fonction.primitives import *
from fonction.liste.listefeuille import *
from fonction.presence import animalPresent

def ajoute(question, animal1, animal2, monArbre):
    if  not animalPresent(animal1,monArbre):
        return monArbre


    if estFeuille(monArbre):
        if animal1 == monArbre:
            return creerArbre(question,animal1,animal2)
        else:
            return monArbre

    return [monArbre[0], ajoute(question,animal1,
            animal2,filsGauche(monArbre)),
            ajoute(question,animal1,animal2,filsDroit(monArbre))]