from fonction.primitives import *
from fonction.ajoute import *
import pickle
def jeu1(monArbre):
    animal_choisit = input("choisir un animal : ")
    while not estFeuille(monArbre):
        reponse = input(monArbre[0])
        if reponse == 'oui':
            monArbre = filsGauche(monArbre)
        elif reponse == 'non':
            monArbre = filsDroit(monArbre)
        else:
            print("il faut répondre par oui ou non")
    print(f'ton animal est un(e) {monArbre}')


def jeu2(monArbre):
    global nouveau_arbre
    arbreNonModifier =monArbre
    animal_choisit = input("choisir un animal : ")
    while not estFeuille(monArbre):
        reponse = input(monArbre[0])
        if reponse == 'oui':
            monArbre = filsGauche(monArbre)
        elif reponse == 'non':
            monArbre = filsDroit(monArbre)
        else:
            print("il faut répondre par oui ou non")
    reponse = input(f'ton animal est un(e) {monArbre}')
    if reponse == 'oui':
        print('je suis trop fort')
    elif reponse == 'non':
        nouvelle_question = input('Ha mince, choisit une question qui'\
        ' est vrai pour l animal que j ai proposé et faux pour ton animal')
        arbreNonModifier = ajoute(nouvelle_question, monArbre, animal_choisit,arbreNonModifier)
    else:
        print('repond oui ou non')

    reponse = input('on rejoue ?')
    if reponse == 'oui':
        jeu2(nouveau_arbre)
    else:
        with open('monArbreAnimaux.pff', 'wb') as monFichier:
            pickle.dump(arbreNonModifier, monFichier)






