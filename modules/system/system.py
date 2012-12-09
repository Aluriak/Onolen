# -*- coding: utf-8 -*-

# Contient des pré-déclarations utilisées par tous les autres 
#       composantes et modules.



##############################
#       IMPORTS              #
##############################
# LIBS
import irclib, ircbot
import threading
import thread
import time
import re # regex
from random import randint, choice
try:
    import cPickle as pickle 
except:
    import pickle 



##############################
#       DECLARATIONS         #
##############################
#
# ONOLEN
#
ONOLEN_Nom = "Onolen"
ONOLEN_Presentation = "Je suis un robot IRC créé par aluriak. Contactez-le pour plus d'informations."
ONOLEN_Naissance = "15/11/2012 à 14h"
ONOLEN_Allegance = 1 # allégance au Gwand Kiwi !
ONOLEN_Patience = 5*60 # nb de secondes durant lesquelles Onolen ne fait rien
ONOLEN_Soutenu = 5 # plus c'est grand, moins Onolen utilise les interjections
ONOLEN_Master = "aluriak"

#
# INFORMATIONS CONNECTION
#
NET_Network = "irc.freenode.net"
NET_Port = 6667
NET_Chan = "#spi2011"
NET_Nick = "Onolen"
NET_Name = "Onolen"

#
# GUI INTERNE
#
GUI_MainMenu = """
1. Message public
2. Commandes
3. Admin
4. Arrêt 
"""
GUI_CommandeMenu = """
1. Message public
2. Message privé
3. Insulter
4. Annuler
"""
GUI_AdminMenu = """
1. Liste des fiches
2. Liste des users actuels
3. Annuler
"""





#
# BASE DE DONNÉES
#
# COMMANDES
COM_QUIT = "reposes-toi maintenant"
COM_MOD_LANCEDES = "lances "
COM_BLAGUE = "blague !"
COM_TODO = "todo "
# REGEX IDENTIFIANTS DES COMMANDES
# record message
REG_MSG_REC = re.compile(r"[dD]is\ +(à|a)\ +([^\ ]+)\ +que\ +(.+)") 
# messages
REG_DICE = re.compile(r"(([0-9]+)d([0-9]+))+") # jouer des dés (1d2 3d8 6d1)
# Todo Liste
REG_TODOL_AFF = re.compile(r"todo +aff.*") # afficher une entrée
REG_TODOL_ADD = re.compile(r"todo +add +(.+)") # ajouter une entrée à la todol
REG_TODOL_DEL = re.compile(r"todo +del +([0-9]+)") # supprime une entrée
REG_TODOL_CHECK = re.compile(r"todo +check +([0-9]+)") # checker une entrée
REG_TODOL_CUT = re.compile(r"todo +cut +([0-9]+) +([^/]+)/([^/]+)") 
REG_TODOL_MERGE = re.compile(r"todo +merge +(.*)/ *([0-9]+) */ *([0-9]+)")
# RACCOURCIS DE COMMANDES
COM_QUIT_r = "gododo"

# Fichiers
FILE_ERR = "erreur.txt"
FILE_OUT = "log"
FILE_FICHE = "fiches/fiches" # contient les fiches de personnes

# Indications de canal
CANAL_LeadKiwi = "Le Gwand Kiwi est leader du canal !"
CANAL_LeadBanane = "La Granbe Banane est leader du canal !"
CANAL_LeadIndecis = "Les indécis sont les leaders de canal !"

# listes de messages prédéfinis par contextes
# pour dire bonjour
BDD_SalutIN = (
    "Salut",
    "Salutations",
    "Bonjour",
    "Bien le bonjour",
    "Oya",
    "Hola",
    "Hoplà kariboo",
    )
# Pour dire au revoir
BDD_SalutOUT = (
    "Salut",
    "Au revoir",
    "A+",
    "bye",
    )
# pour jurer
BDD_Juron = (
    "Scheisse",
    "Countescount",
    "Groummf",
    "Bile de poing",
    )
# pour lâcher un mot ou une expression
BDD_Interjection = (
    "Par les anneaux de Saturne",
    "Par le boson de Higgs",
    "Par la barbe de Darwin",
    "Par la poussière de l'Étoile",
    "Par la malveillance de Némésis",
    "Par les gènes de mes ancêtres",
    )
# Nom donné à l'ensemble des utilisateurs du canal
BDD_NomAssemblee = (
    "les gens",
    "tout le monde",
    "l'assemblée",
    "les ircistes",
    )
# quand l'accès n'est pas autorisé
BDD_SudoManquant = (
    "Et puis quoi encore ?",
    "Essayes avec sudo pour voir ?",
    "J'ai pas envie !",
    "Cause toujours !",
    "*Onolen n'est pas affecté par ton test de bluff*",
)
# Pour justifier le départ d'irc
BDD_JustificationAuRevoir = (
    "on a besoin de moi ailleurs !",
    "l'affreux docteur Côtdeporc à encore frappé !",
    "ma grand-mère a pété une durite !",
    "j'ai un rendez-vous galant avec une jolie GPU !",
    "je vais à la Maison des Jeunes Compilateurs !",
    "le chat de mon voisin s'est encore perdu dans l'arborescence...",
    "je dois battre mon record à space invaders !",
    "je dois faire des course à l'hypercube !",
    "j'ai du ménage à faire, mon ventilo ne suffit plus...",
    "ma grand-mère fait du vélo en tutu à paillette !",
)
# Manifestation de joie
BDD_ManifJoie = (
    "Youpi",
    "Génial",
)
# Blague
BDD_Blague = (
    "Pour qu'un projet git tombe à l'eau, il faut lancer la commande git plouf",
    "Mon objet oiseau fait GUI-GUI",
    "C'est une l'histoire d'un pingouin qui respirait par les fesses. Un jour il s'assoie, et il meurt.",
    "C'est l'histoire d'un pingouin qui lève une jambe. Comme il trouve ça drôle, il lève l'autre. Et il tombe.",
    "L'évolution a permis l'apparition du taxon souris usb. Une mutation bienvenue car le taxon des souris ps3 est en voie de disparition.",
    "C'est l'histoire d'un octet qui rentre dans un processeur : clock !",
    "Quand ma carte-mère me dit de venir à table, elle lock le sémaphore sur toutes les ressources, pour m'obliger à join le thread \"miam_time\".",
    "La carte-mère à la carte graphique : \"Alors ? C'est qui qu'a la plus grosse ?\". En parlant de leurs ventilateur, évidemment !",
    "La carte-mère à ses filles : \"le père BIOSël distribut des protocoles aux carte-filles qui sont sages pendant les reboot\".",
    "Le mammouth est un animal à poil laineux. A poil Laineux ! A poil Laineux ! A poil Laineux !",
    "Vous connaissez l'histoire du BIOS qui dit \"No keyboard detected. Press F5 to continue\" ?",
)
# Formules de remerciement
BDD_Merci = (
    "Merci",
    "Danke Shön",
)
# Formules de réponse au remerciement
BDD_DeRien = (
    "you welcome",
    "cadeau de la maison",
    "no problemo",
    "avec les palmes",
)
# Adjectifs divers
BDD_Adjectifs = (
    "gargantuesque",
    "emberlifibrouillant",
    "énerxaspérant",
    "joyeux",
    "bienheureux",
    "filant",
    "avec les palmes,"
)
# Noms prédéfinis
BDD_Noms = (
    "Jean-Michel",
    "Jean-Michel²",
    "Le Grand Pot-Au-Feu",
    "Bobbit le Hilbo",
    "El Kariboo",
    "Le LHC",
    "Jean-Bob",
    "Plouf la grenouille",
    "Les palmes",
)
# accesseurs
def BDD_getSalutIN():
    return choice(BDD_SalutIN)
def BDD_getSalutOUT():
    return choice(BDD_SalutOUT)
def BDD_getJuron():
    return choice(BDD_Juron)
def BDD_getInterjection():
    return choice(BDD_Interjection)
def BDD_getNomAssemblee():
    return choice(BDD_NomAssemblee)
def BDD_getSudoManquant():
    return choice(BDD_SudoManquant)
def BDD_getJustificationAuRevoir():
    return choice(BDD_JustificationAuRevoir)
def BDD_getBlague():
    return choice(BDD_Blague)
def BDD_getMerci():
    return choice(BDD_Merci)
def BDD_getDeRien():
    return choice(BDD_DeRien)
def BDD_getAdjectifs():
    return choice(BDD_Adjectifs)
def BDD_getNoms():
    return choice(BDD_Noms)







#
# METHODES 
#
# Ecrit une erreur dans le fichier d'erreur
def FLUX_ERREUR(erreur):
    try:
        ferr = open(FILE_ERR, "a")
        ferr.write(erreur+"\n")
        print "Erreur détectée et explicitée dans FILE_ERR"
    except:
        print "/!\\"
        print "###########################################"
        print "# ERREUR CRITIQUE : FILE_ERR non ouvert ! #"
        print "###########################################"
        print "/!\\"
    finally:
        ferr.close()



