# -*- coding: utf-8 -*-

#########################
#       IMPORTS         #
#########################
from modules.system.system import *




###########################
#       LANCE DES         #
###########################

# Retourne une liste des chaînes à afficher
# Attend la directive composés de "([0-9]d[0-9])+" 
#       séparés par un espace
# Et retourne les résultats des ancés de dés en conséquence
# Exemple : "1d6 10d4 5d9", renvois les résultats 
#       des lancés demandés
# Renvois la liste des chaînes à aficher, dans l'ordre
def lanceDes(directive):
    # liste de chaînes à retourner
    listeChaine = [] # vide au départ
    # si on retrouve le motif dans la directive
    if REG_DICE.search(directive):
        # capture des éléments trouvés par regex
        result = REG_DICE.findall(directive)
        sommeTotale = 0 # somme de tous les dés lancés
        # pour chacun des groupes de dés demandés
        for i in range(0, len(result)):
            nbDes = result[i][1]
            if int(nbDes) > 10: # simple sécurité
                nbDes = "10"
            szDes = result[i][2]
            if int(szDes) > 100000: # simple sécurité
                nbDes = "100000"
            # pas d'affichage si le dés doit être lancé 0 fois
            if int(nbDes) > 0:
                # initialisation de la chaine et du compteur
                chaine = nbDes+" dés de taille "+szDes+": "
                sommeGroupe = 0 # pour afficher la somme des valeurs des dés
                # affichage de tous les résultats sauf le dernier
                for t in range(0, int(nbDes)-1):
                    valeurDe = randint(1,int(szDes))
                    chaine += str(valeurDe)+"/"
                    sommeGroupe += valeurDe
                # affichage du dernier, sans slash à la fin
                valeurDe = randint(1,int(szDes))
                chaine += str(valeurDe)
                sommeGroupe += valeurDe
                # on ajoute le total à la chaîne
                chaine += "\t\tTotal = "+str(sommeGroupe)
                sommeTotale += sommeGroupe
                # on ajoute la chaîne à la liste des chaînes à afficher
                listeChaine.append(chaine)
        # on ajoute à la fin la chaine contenant la somme totale de tous les dés lancés
        # à condition qu'il y ais au moins deux sortes de dés
        if len(result) > 1:
            listeChaine.append("Total = "+str(sommeTotale))
    return listeChaine



