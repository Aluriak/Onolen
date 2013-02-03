# -*- coding: utf-8 -*-
# =====================================================
#
# ONOLEN_Reaction
#
# Gère les réactions d'Onolen selon 
#       les messages envoyés par 
#       d'autres utilisateurs, 
#       en public ou privé
#
# =====================================================


#
# IMPORTS
#
from modules.system.system import *
from modules.lanceDes.lanceDes import *
from modules.todolist.todolist import *
from modules.personne.Personne import *



#
# METHODE D'ACCES
#


#
# CLASSE 
#
class Onolen_Reaction(ircbot.SingleServerIRCBot):
    """
    Classe Réaction; gère tous les aspects réactifs d'onolen
    Exploite les modules irclib et ircbot.
    """

    def __init__(self, Onolen, modeDebug):
        self.nom = ONOLEN_Nom
        self.presentation = ONOLEN_Presentation
        self.DEBUG = modeDebug
        self.network = NET_Network 
        self.port = NET_Port
        self.chan = NET_Chan
        self.listeUsers = {} # clef = user; valeur = bool(vrai si user actif)
        self.fiche = getFiches() # on récupère le dico de Fiches
        self.todol = todoList.charger()
        # en attente si Onolen l'a questionné et qu'il n'a pas encore répondu
        self.Onolen = Onolen
        # connection/création du programme de bot
        ircbot.SingleServerIRCBot.__init__(self,
                                           [(self.network, self.port)],
                                           self.nom,
                                           self.presentation)


    
    # connection au serveur réussie
    def on_welcome(self, server, ev):
        # on rejoins les chats prévus
        self.rapport("O> Serveur "+self.network
                     +" rejoint le "+time.ctime(time.time()))
        server.join(self.chan)
        self.server = server # on enregistre bien le serveur retourné
        self.Onolen.server = server # on donne l'identitié du serveur 
        self.Onolen.chan = self.chan
        #   à Onolen
        self.verification()


    # nouveau message sur le chat
    def on_pubmsg(self, server, ev):
        # récupération des données importantes
        auteur = irclib.nm_to_n(ev.source())
        message = ev.arguments()[0]
        canal = ev.target()
        self.rapport(auteur+": "+message+"\n")
        self.priseEnCompte(auteur) # procédure de rise en compte de l'auteur
        # passage en sudo de la commande si demandé par le maître
        sudo = auteur == ONOLEN_Master
        # si le message est adressé à Onolen (commence par "Onolen: ")
        if message[0:2+len(self.nom)] == (self.nom+": "):
            # on isole le contenu intéressant du message
            message = message[2+len(self.nom):]

            # COMMANDES SUDO
            if(message == COM_QUIT or message == COM_QUIT_r):
                if sudo:
                    self.Onolen.Termine = True
                else:
                    self.sendMessage(BDD_getSudoManquant())
            elif message == "autre commande sudo":
                pass

            # COMMANDES NORMALES
            # module lanceDes
            if message[0:7] == COM_MOD_LANCEDES: 
                # on envoie la partie du message attendue par le message
                # renvois une liste des chaînes à afficher
                listeSortie = lanceDes(message[7:])
                for i in listeSortie:
                    # on envois cette ligne à IRC, sans interjection
                    self.sendMessage(i, False)
            elif message == COM_BLAGUE:
                self.sendMessage(BDD_getBlague())
            # module todo list
            elif message[0:5] == COM_TODO:
                # execution de la commande, et reotur des chaînes à afficher
                listReturn = self.todol.execute(message, auteur) 
                # on affiche ces chaînes. Seule la première peux avoir une
                # interjection
                firstIteration = True
                for e in listReturn:
                    self.sendMessage(e, firstIteration)
                    firstIteration = False
            elif message == "autre commandes normale":
                pass

            # COMMANDES REGEX
            # enregistrement de message
            if REG_MSG_REC.search(message):
                self.ajoutMessagerie(auteur, message)
            elif message == "autre commande regex":
                pass

        # MESSAGE NON ADRESSÉ EXPLICITEMENT A ONOLEN
        # Communication de joie, sauf si c'est teuse ou Onolen
        elif message == "\o/" and auteur != self.nom and auteur != "teuse":
                self.sendMessage(message, False)



    # nouveau message privé
    def on_privmsg(self, server, ev):
        # récupération des données importantes
        auteur = irclib.nm_to_n(ev.source())
        message = ev.arguments()[0]
        result = "O> Message privé reçu de "+auteur+": \""+message+"\"\n?>"
        self.rapport(result)
        print result


    # nouvel arrivant sur le canal
    def on_join(self, server, ev):
        arrivant = irclib.nm_to_n(ev.source())
        # si c'est Onolen lui-même qui est arrivé
        if arrivant == self.nom:
            self.rapport("O> Canal "+self.chan+
                         " rejoint le "+time.ctime(time.time()))
            self.Onolen.HL = False # Onolen est désormais en ligne
            self.saluer(BDD_getNomAssemblee()) # on salue la foule !
        # si l'arrivant est connu
        elif self.fiche.has_key(arrivant):
            self.rapport("O> Nouvel arrivant : "+arrivant)
            self.listeUsers[arrivant] = 1 # cet user est actif !
            self.saluer(arrivant) # on salue l'arrivant
        # si non connu, on se présente
        else:
            self.rapport("O> Nouvel arrivant, inconnu au bataillon : "+arrivant)
            self.rencontrer(arrivant)



    # redéfinition de cette méthode retournant sinon des infos sur 
    #   le créateur de la lib
    def get_version(self):
        return self.presentation


    # Saluer la cible lorsqu'elle arrive
    def saluer(self, cible):
        if not self.DEBUG:
            salut = BDD_getSalutIN()+" "+cible+" !"
            self.sendMessage(salut)


    # Gère la rencontre avec une nouvelle personne
    def rencontrer(self, cible):
        self.saluer(cible) # on salue l'arrivant
        self.sendMessage(self.presentation) # on se présente
        # on lui créé une fiche
        self.fiche[cible] = Fiche(cible)
        

    # Rencontre et salue la cible si elle n'était pas connue
    def priseEnCompte(self, cible):
        # si l'utilisateur est connu, et qu'il ne c'était pas encore manifesté
        if self.listeUsers.has_key(cible) and (
            (not self.listeUsers.has_key(cible)) 
            or self.listeUsers[cible] == 0):
            saluer(cible) # on le salue !
        # on indique dans le dictionnaire des connectés que l'utilisateur
        #       est actif, et donc considérable
        self.listeUsers[cible] = 1
        # si jamais il n'y avais pas d'entrée pour ce nom-là, on la rencontre
        if not self.fiche.has_key(cible):
            self.rencontrer(cible)
        # pour chaque message de la messagerie
        for auteur in self.fiche[cible].messagerie:
            self.sendMessage(cible+": "+auteur+" t'a laissé ce message : \""
                             +self.fiche[cible].messagerie[auteur]+"\"")
        # et suppression des messages de la messagerie !
        self.fiche[cible].messagerie.clear()

    

    # Saluer la cible, lorsqu'elle part
    def auRevoir(self, cible):
        if not self.DEBUG:
            salut = BDD_getSalutOUT()+" "+cible+" !"
            self.sendMessage(salut)


    # Surcouche de la méthode d'envois de message d'Onolen
    # avecAlteration vrai si on peut ajouter une interjection
    def sendMessage(self, message, interj=True):
        # on détermine une éventuelle altération du message, avec notamment 
        # une interjection. Une chance sur ONOLEN_Soutenu
        if (not self.DEBUG) and interj and randint(0,ONOLEN_Soutenu) == 1:
            # on passe la première lettre en minuscule si c'est possible
            message = message[0].lower() + message[1:]
            # on ajoute l'interjection
            message = BDD_getInterjection()+", "+message
        # Envois du message, modifié ou non
        self.Onolen.sendMessage(message)
        self.rapport("Onolen: "+message+"\n")


    # Effectue vérifications et calculs pour gérer la demande de message 
    # par auteur avec le message
    def ajoutMessagerie(self, auteur, message):
        result = REG_MSG_REC.findall(message)
        dest = result[0][1]
        msg = result[0][2]
        # si l'auteur s'envois un message à lui-même, ou à Onolen
        if dest == auteur or dest == self.nom: 
            self.Onolen.sendInsulte(auteur)
        else:
            # on ajoute le message à la messagerie du destinataire
            # s'il est connu, il est dans les fiches
            if self.fiche.has_key(dest):
                self.fiche[dest].messagerie[auteur] = msg
                self.sendMessage("Je dirais à "+dest+
                                 ", de la part de "+auteur+" que "+msg)
            else:
                self.sendMessage("Je ne crois pas avoir déjà rencontré "
                                 +dest+"...")


    # Envois ses observations dans un fichier convenu à l'avance
    def rapport(self, message):
        fichier = open(FILE_OUT, "a")
        try:
            fichier.write(message)
        finally:
            fichier.close()


    # Base "l'intelligence" d'Onolen
    # se rappelle en moyenne toutes les ONOLEN_Patience secondes
    def reflexion(self):
        # on se rappelle
        self.server.execute_delayed(randIntervalle(ONOLEN_Patience), 
                                    self.reflexion)



    # si quelqu'un est kické
    def on_kick(self, serv, ev):
        pass


    # arrête Onolen si il doit s'arrêter, ou se rappelle dans quelques secondes
    def verification(self):
        if self.Onolen.Termine:
            if not self.DEBUG:
                goodbye = "Désolé, je dois partir; " + \
                        BDD_getJustificationAuRevoir()
                self.sendMessage(goodbye)
            self.rapport("O> Déconnection du serveur "+self.network+
                         " le "+time.ctime(time.time()))
            # on enregistre les nouvelles fiches
            setFiches(self.fiche)
            self.todol.enregistrer()
            # dernière action, et fin du script
            if not self.DEBUG:
                goodbye = str(self.auRevoir(BDD_getNomAssemblee()))
            else:
                goodbye = " "
            self.die(goodbye)
        else:
            self.server.execute_delayed(2, self.verification)



