# -*- coding: utf-8 -*-



#
# METHODES SECONDAIRES
#
# Demande un entier à l'utilisateur
# renvois -1 en cas de problème
def captureEntier():
    rep = -1
    try: 
        rep = int(raw_input("?>"))
    except:
        rep = -1
    return rep

# Demande une chaîne l'utilisateur
# renvois chaîne vide en cas de problème
def captureChaine():
    rep = ""
    try: 
        rep = raw_input("?>")
    except:
        rep = ""
    return rep

# Renvois un nombre aléatoire contenu entre
# (N/2) et (N + N/2)
def randIntervalle(N):
    return N/2 + random.randint(0,N)




