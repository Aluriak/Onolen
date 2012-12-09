# -*- coding: utf-8 -*-
# =====================================================
#
# ONOLEN
#
# Gère les réactions d'Onolen selon 
#       les messages envoyés par 
#       d'autres utilisateurs, 
#       en public ou privé, et lance éventuellement 
#       le thread de reflexion
#
# =====================================================


#
# IMPORTS
#
from modules.system.system import *
from modules.insulte.insulte import *
from modules.personne.Personne import *
from modules.lanceDes.lanceDes import *
from modules.reaction.reaction import *


#
# METHODES D'ACCES
#



#
# CLASSE MERE
#
# classe mère d'Onolen
class Onolen(threading.Thread):
    """
    Classe Mère; 
    gère tous les aspects réactifs et reflexifs d'onolen
    Créé et gère la classe ircbot
    """

    # HL est à vrai si Onolen doit rester Hors Ligne
    def __init__(self, modeDebug):
        threading.Thread.__init__(self)
        self.nom = ONOLEN_Nom
        self.presentation = ONOLEN_Presentation
        self.modeDebug = modeDebug
        self.chan = 0
        self.HL = True # vrai tant que hors ligne
        self.Termine = False # faux tant qu'Onolen doit continuer
        # création de la réaction
        self.bot = Onolen_Reaction(self, self.modeDebug)

    # Fonction de démarrage de thread
    def run(self):
        # lancement de la réaction
        self.bot.start()


    # envoie un message sur le chan
    def sendMessage(self, message):
        dest = self.chan
        self.server.privmsg(dest, message)
        # TODO: indique l'heure à laquelle ce message à été envoyé
        # permet de savoir depuis cb de temps Onolen n'a pas été actif, 
        # et donc si la méthode réflexion peut entrer en jeu


    # envoit une insulte sur le chan demandé, adressé à la cible
    def sendInsulte(self, cible):
        self.server.privmsg(self.chan, insultePour(cible))


    # envoie un messge privé
    def sendPrivMessage(self, destinataire, message):
        self.server.privmsg(destinataire, message)



    # arrête Onolen le plus proprement possible
    def Fin(self):
        self.Termine = True


