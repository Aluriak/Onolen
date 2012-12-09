# -*- coding: utf-8 -*-
# Contient les procédure de créations d'insultes

#
# IMPORTS
#
from bdd import * # pour générer des insultes facilement




#
# METHODES D'ACCES
#
# créer une insulte pour insulter la cible
def insultePour(cible):
    insulte = cible + ": " + genererInsulte()
    return insulte


if __name__ == '__main__':
    print insultePour("Personne en particulier")
