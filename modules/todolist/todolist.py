# -*- coding: utf-8 -*-

#########################
#       IMPORTS         #
#########################
from modules.system.system import *




##########################
#       TODOLIST         #
##########################

# Gestion d'une TODOliste. Commandes à adresser :
#       - todo, pour afficher les entrées et leurs index
#       - todo add <intitulé>, pour ajouter l'entrée indiquée
#       - todo check <id>, pour dire que l'entrée d'index id a été faite
#       - todo clean, pour retirer toutes les entrées checkées
#       - todo cut <id> <intitulé>/<intitulé> pour découper l'entrée 
#               d'index id en deux autres entrées, 
#               d'intitulés séparés par des virgules.
#       - todo merge <id>/<id> pour fusionner les deux entrées d'index id
# Pour chaque entrée, on enregistre : 
#       - intitulé
#       - auteur
#       - bool isChecked (vrai si checkée)
#       - id


class todoEntree():
    def __init__(self, intitule, auteur, ID, checked = False):
        self.intitule = intitule
        self.auteur = auteur
        self.isChecked = checked
        self.ID = ID



class todoList():
    def __init__(self):
        self.entree = [] # liste des entrées
        self.IDLibre = 0 # prochain id d'entree à attribuer


    # méthode publique, gère en fonction de la commande "todo <directive>"
    # (attend seulement la <directive>)
    # retourne une liste de chaînes à afficher
    def execute(self, directive, auteur):
        listeRetour = [] # liste des chaînes à envoyer
        # Affichage de la liste
        if REG_TODOL_AFF.search(directive): 
            for e in self.entree:
                chaine = "\t"+str(e.ID)+". "+e.intitule+" ("+e.auteur+")"
                if e.isChecked:
                    chaine = chaine + " [CHECKED]"
                listeRetour.append(chaine)
            # si la liste est vide, on l'indique
            if listeRetour == []:
                listeRetour = ["La todo list est vide !"]
            else: # si il y a au moins une entrée
                listeRetour.insert(0, "Voilà les "+str(len(self.entree))+\
                                   " entrées de la liste :")
        # Ajout d'une entrée
        elif REG_TODOL_ADD.search(directive):
            result = REG_TODOL_ADD.findall(directive)
            self.add(result[0], auteur)
            listeRetour.append("Entrée "+result[0]+" de "+auteur+" enregistrée")
        # Suppression d'une entrée
        elif REG_TODOL_DEL.search(directive):
            result = REG_TODOL_DEL.findall(directive)
            if self.supprimerID(int(result[0])):
                listeRetour.append("Entrée d'id "+result[0]+\
                                   " supprimée")

        # Découpage d'une entrée
        elif REG_TODOL_CUT.search(directive):
            result = REG_TODOL_CUT.findall(directive)
            idACouper = int(result[0][0]) # id de la directive à cuter
            entreeA = result[0][1] # première entrée
            entreeB = result[0][2] # seconde entrée
            # parcours des entrées jusqu'à trouver la bonne id
            for e in self.entree:
                # on modifie l'entrée ciblée
                if e.ID == idACouper:
                    # on modifie l'entrée à couper
                    e.intitule = entreeA
                    # et on ajoute l'entrée B
                    self.add(entreeB, auteur) 
                    listeRetour.append("Entrée d'id "+str(idACouper)+" coupée")
            

        # Check d'une entrée
        elif REG_TODOL_CHECK.search(directive):
            result = int(REG_TODOL_CHECK.findall(directive)[0])
            for e in self.entree:
                if(e.ID == result):
                    self.check(e)
                    listeRetour.append("Entrée d'id "+str(result)+\
                                       " checkée")


        # Uncheck d'une entrée
        elif REG_TODOL_UNCHECK.search(directive):
            result = int(REG_TODOL_UNCHECK.findall(directive)[0])
            for e in self.entree:
                if(e.ID == result):
                    self.check(e, False)
                    listeRetour.append("Entrée d'id "+str(result)+\
                                       " uncheckée")


        # Clear, suppression des entrées checkées
        elif REG_TODOL_CLEAR.search(directive):
            self.clean()
            listeRetour.append("Entrées checkées supprimées")


        # Merge de deux entrées
        elif REG_TODOL_MERGE.search(directive):
            result = REG_TODOL_MERGE.findall(directive)
            entreeMergee = result[0][0] # intitulé du merge
            idAMergerA = int(result[0][1]) # id de la première entrée à merger
            idAMergerB = int(result[0][2]) # id de la seconde
            # parcours des entrées jusqu'à trouver l'id de la première entrée
            for e in self.entree:
                # on modifie l'entrée ciblée
                if e.ID == idAMergerA:
                    # on modifie l'entrée à couper
                    e.intitule = entreeMergee
                    # suppression de la deuxième entrée
                    self.supprimerID(idAMergerB)
                    listeRetour.append("Merge des id "+str(idAMergerA)+" et "+\
                                       str(idAMergerB)+" effectué")


        # on renvois la liste de chaînes à afficher
        return listeRetour



    # ajoute l'entrée de type todoEntree à la liste et en modifie l'id pour 
    # qu'il ai une bonne valeur
    def add(self, intitule, auteur):
        entree = todoEntree(intitule, auteur, self.IDLibre)
        self.entree.append(entree)
        self.IDLibre += 1 # id suivant

    # check l'entree demandée, ou la remet en normal si demandé explicitement
    def check(self, entree, check = True):
        entree.isChecked = check

    # Retire toutes les entrées checkées
    def clean(self):
        interListe = [] # liste intermédiaire
        for i in self.entree:
            # si l'entree n'est pas checkée, on la met dans l'intermédiaire
            if not i.isChecked:
                interListe.append(i)
        # on utilise maintenant l'interListe
        self.entree = interListe


    # Supprime toutes les entrées d'id indiquées
    def supprimerID(self, idASupprimer):
        suppressionEffectuee = False
        # on parcours les entrées, jusqu'à trouver celle à supprimer
        it = 0
        for e in self.entree:
            # on n'ajoute l'entrée que si elle n'est pas à l'id ciblé
            if e.ID == idASupprimer:
                del self.entree[it]
                suppressionEffectuee = True
            it += 1
        return suppressionEffectuee




