# -*- coding: utf-8 -*-

#
# IMPORTS
#
from modules.system.system import *
from modules.todolist.todolist import *
from modules.personne.Personne import *
from fctAnnexes import *
# module pickle : pour enregistrer rapidement des structure de données dans des fichiers
try:
    import cPickle as pickle # on essaye d'importer le module cPickle, plus rapide, sous le nom de pickle
except:
    import pickle # si ça foire, on utile pickle normal

# objectif : remplir rapidement la bdd d'Onolen







#
# CREATION FICHES DE BASE
#
# Création d'un dictionnaire avec pour seule fiche celle d'Onolen
# Dictionnaire enregistré avec Pickle, compatible lecture par Onolen
def creerFichesBase():
    # on créé un dictionnaire et on range la fiche d'Onolen dedans
    dic = {"Onolen":Fiche("Onolen", "Onolen", Allegance.Kiwi, Sexe.RobotM)}
    # ajout du maître 
    dic["aluriak"] = Fiche("aluriak", "lucas", Allegance.Kiwi, Sexe.Homme)
    # on met ce dictionnaire dans le fichier des fiches
    try:
        fileFiches = open("ficheDeBase", "w")
        # écriture avec pickle
        pickle.dump(dic, fileFiches)
        fileFiches.close()
    except:
        print "Oops ! problème d'ouverture du fichier ficheDeBase !"



Menu = """1. Reinitialiser Fiches
2. Ajouts
3. TODO
4. Quitter
"""



#
# MAIN
#
if __name__ == "__main__":
    termine = False
    # GUI
    while(not termine):
        print Menu
        rep = captureEntier()
        # REINITIALISER FICHES
        if(rep == 1): 
            print "Etes vous sûr ? (o/*)"
            rep = captureChaine()
            if(rep == "o"):
                creerFichesBase()
                print "Fiches réinitialisées"
            else: 
                print "abandon"
        # AJOUTS BDD
        elif rep == 3:
            pass
        # FIN
        elif(rep == 4):
            termine = True
        # TODO
        else:
            print "Incorrect"
    creerFichesBase()


