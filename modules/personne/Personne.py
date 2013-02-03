# -*- coding: utf-8 -*-
#########################
#       IMPORTS         #
#########################
from modules.system.system import *


##########################
#       PERSONNE         #
##########################
# Structure de données pour une personne

# classe d'allégance, à la banane ou au kiwi
# Très simple, juste pour alléger l'écriture
class Allegance():
    Kiwi = 1
    Banane = 0
    Indecis = -1
# Autre classe énumérative
class Sexe():
    Femme = 2
    Homme = 1
    Inconnu = 0
    RobotM = -1
    RobotF = -2


# Classe de fiche de personne
class Fiche():
    def __init__(self, pseudo, nom='', 
                 allegance=Allegance.Indecis, 
                 #dateN = time.ctime(time.time()), 
                 sexe=Sexe.Inconnu):
	self.pseudo = pseudo
	self.nom = nom
	self.allegance = allegance
        #self.dateNaissance = dateN
        #self.AnnivSouhaite = False
        self.sexe = sexe
        # dictionnaire des messages à transmettre, 
        # sous la forme clef = expéditeur, valeur = message
        self.messagerie = {}



    





#
# METHODES D'ACCES
#
# Renvois le dictionnaire de Fiche (clef = utilisateur, valeur = Fiche)
def getFiches():
    # dictionnaire vide
    fiches = {}
    # on tente d'ouvrir le fichier et de charger le dictionnaire de fiches
    try:
        fileFiches = open(FILE_FICHE, "r")
    except:
        FLUX_ERREUR("Personne.getFiches(0): erreur d'ouverture de FILE_FICHE") 
        return fiches
    # lecture avec pickle
    fiches = pickle.load(fileFiches)
    fileFiches.close()
    # on retourne le dictionnaire de fiches
    return fiches


# Inscrit le dictionnaire de Fiches dans le fichier
# écrase les données précédentes
def setFiches(fiches):
    try:
        fileFiches = open(FILE_FICHE, "w")
    except:
        FLUX_ERREUR("Personne.setFiches(1): erreur d'ouverture de FILE_FICHE") 
        return
    # écriture avec pickle
    pickle.dump(fiches, fileFiches)
    # et fermeture
    fileFiches.close()

