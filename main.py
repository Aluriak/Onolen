# -*- coding: utf-8 -*-

#########################
#       IMPORTS         #
#########################
# toutes les directives de préparations et d'importations
#from modules.system.system import *
# autres modules
from modules.system.system import *
from fctAnnexes import *
from Onolen import * 



#########################
#       MAIN            #
#########################
# Création des threads d'Onolen
#       - Principal: classe Onolen
#               - ircbot
#               - reflexion
#       - Interne: boucle de gestion interne


# Menu de gestion interne d'Onolen
termine = False
DEBUG = False
Onolen = Onolen(DEBUG) # contiendra l'instance de classe d'Onolen
# démarrage !
Onolen.start()

# on attend qu'Onolen soit connecté
print "O>..."
while Onolen.HL:
    time.sleep(1)
print "O> Salut !"



# GUI
while(not termine and not Onolen.Termine):
    print(GUI_MainMenu)
    rep = captureEntier()
    # Message
    if(rep == 1): 
        print "O> Message à envoyer : "
        rep = captureChaine()
        if(rep == ""):
            print "Message non envoyé"
        else: 
            Onolen.sendMessage(rep)
    # Commandes
    elif(rep == 2): 
        print(GUI_CommandeMenu)
        rep = captureEntier()
        # Message public
        if(rep == 1): 
            print "O> Message à envoyer : "
            rep = captureChaine()
            if(rep == ""):
                print "Message non envoyé"
            else:
                try:
                    Onolen.sendMessage(destinataire, message)
                except:
                    print "Message non envoyé"
        # Message privé
        elif(rep == 2):
            print "O> Destinataire : "
            destinataire = captureChaine()
            if(destinataire == ""):
                print "Message non envoyé"
            else:
                print "O> Message à envoyer : "
                message = captureChaine()
                if(message == ""):
                    print "Message non envoyé"
                else:
                    try:
                        Onolen.sendPrivMessage(destinataire, message)
                    except:
                        print "Message non envoyé"

        # Insulte
        elif(rep == 3):
            print "O> Destinataire : "
            destinataire = captureChaine()
            if(destinataire == ""):
                print "Annulé"
            else:
                Onolen.sendInsulte(destinataire)
        # Annuler
        elif(rep == 4):
            pass
        else:
            print "Valeur incorrecte"

    # Admin
    elif(rep == 3): 
        print(GUI_AdminMenu)
        rep = captureEntier()
        # Dresse la liste des fiches
        if(rep == 1): 
            for i in Onolen.bot.fiche:
                print Onolen.bot.fiche[i].pseudo
        # Dresse la liste des users actuels
        elif(rep == 2):
            for i in Onolen.bot.listeUsers:
                print i
        # Annuler
        elif(rep == 3):
            pass
        else:
            print "Valeur incorrecte"
    # Arrêt
    elif(rep == 4): 
        rep = raw_input("O> Confirmez l'arrêt (o/n) : ")
        if(rep == "o"):
            termine = True
    # Invalide
    else:
        print "Valeur incorrecte"


# arrêt des processus
Onolen.Fin()










