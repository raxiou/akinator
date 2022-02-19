from fonction.liste.listefeuille import *
from fonction.liste.lesquels import *
from fonction.presence import *
from fonction.compte import *
from fonction.ajoute import *
from fonction.Jeu import *

try:
    with open('monArbreAnimaux.pff', 'rb') as monFichier:
        monArbre = pickle.load(monFichier)

except:
    monArbre = ['vit_il dans la maison ?', ['a t il des poils ?', \
                ['miaule t il ?', 'chat', 'Hamster'], 'Poisson rouge'], \
                ['est il dangeureux ?', ['vole t il ?', \
                'Frelon', 'Tigre'], 'Herisson']]

jeu2(monArbre)