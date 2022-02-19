from fonction.presence import *
from fonction.primitives import *


def lesquels(question, monAbre):
    if not questionPresent(question, monAbre):
        return []


    else:
        if estFeuille(monAbre):
            return []
        if question == monAbre[0]:
            return listefeuille(filsGauche(monAbre))

        return lesquels(question, filsGauche(monAbre)) + lesquels(question, filsDroit(monAbre))