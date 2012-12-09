# -*- coding: utf-8 -*-
# Contient toutes les données nécessaires à la confection d'insultes

#
# IMPORTS
#
from random import choice, randint


# deux types d'insultes : exclamative (t'es nul) et 
#       interrogatives (tu savais que t'était nul ?)

#insulte de la forme : Interpellation, sortie de liste


#
# METHODES D'ACCES
#
# Génère une insulte 
def genererInsulte():
    # chaine contenant l'insulte
    chaine = ''
    # on choisis entre interrogatif et exclamatif
    if randint(0,1) == 0: # exclamatif
        chaine = choice(liste_prefixe_exclam) + 'que '
        fin = ' !'
    else: # interrogatif
        chaine = choice(liste_prefixe_interrog) + 'que '
        fin = ' ?'

    # insertion de l'insulte et de la ponctuation finale
    chaine += choice(liste_Insulte)
    chaine += fin
    # retour de l'insulte générée
    return chaine



#
# STRUCTURES DE DONNEES
#
# Liste des insultes
liste_Insulte = [
    "t'es qu'une émission de carbone 14",
    "t'es tellement pas attractif que même tes électrons s'en vont",
    "t'es tellement moche que les photons que tu réfléchis diminuent leur durée de vie",
    "t'es tellement pas drôle que même l'hydrogène ne te donne pas une voie éguë",
    "t'es aussi prévisible qu'une équation linéaire du premier ordre",
    "t'es tellement pas sécurisant que t'as tes attributs en public",
    "t'es connecté en socket avec ton propre cerveau pour réfléchir, sauf que vous n'utilisez pas le même protocole",
    "t'es aussi intuitif que la syntaxe polonaise inversée",
    "t'es formaté en UTF-1",
    "t'es aussi sécurisant qu'un segmentation fault",
    "t'es aussi chiant qu'un virus, sauf que lui il est codé pour ça",

    "t'as pas assez de neurones pour faire du multithread",
    "t'as redoublé ta crèche tellement t'es pas adapté à l'intelligence",
    "t'as été codé en brainfuck",
    "t'as breaké une boucle alors que t'étais même pas dedans. C'est con, c'était celle qui relançait les instructions d'intelligence",
    "t'as arrêté ton développement à la prophase",
    "t'as raté le carrefour phylogénique qui sépare le singe de l'homme",
    "t'as jamais réussi à indenter ton code en Python",
    "t'as programmé en procédural avec java",
    "t'as applaudit ACTA",
    "t'as une tronche de consonne fricative vélaire sourde",
    "t'as tellement pas de classe que tu peux même pas faire de POO",

    "ton adressage mémoire s'arrête à 0xFF",
    "ton adresse atitrée, c'est NULL",
    "ton processeur a une datasheet de 2 lignes",
    "ton pc n'a jamais vu le terminal, ni même son émulateur",
    "ton pc tourne sous brainfuck OS",

    "ta méthode parler() n'a pas d'argument",
    "ta carte son ne sait faire que du bruit chiant"
]



# Liste des suffixes d'interpellation interrogatives
liste_prefixe_interrog = [
    "Tu savais ",
    "On t'as déjà dit ",
    "T'avais remarqué ",
    "Tu te rendais compte "
]

# Liste des préfixes d'interpellation exclamatives
liste_prefixe_exclam = [
    "Tout le monde sait ",
    "Il est démontré ",
    "Tu devrais te rappeler ",
    "Oublis pas "
]

# Liste des choix de mode d'insulte
liste_choixMode = [
    "exclamatif",
    "interrogatif"
]






# séparer le comportement du programme module/main
if __name__=='__main__':
    insulte = genererInsulte()
    print(insulte)
