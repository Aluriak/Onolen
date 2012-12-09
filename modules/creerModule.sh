# -*- coding: utf-8 -*-
# Créer un module de nom envoyé en premier argument

# pattern d'un fichier par défaut
filePattern="# -*- coding: utf-8 -*-"



# on attend au moins un argument
# si il y en a d'autres, on fait une boucle de création de fichiers internes du même nom

if [[ $# -lt 1 ]] 
then
    echo "Pas assez d'arguments"
else
    # récupération du nom module
    module=$1
    # nom du fichier
    fichier="${module}/${module}.py"

    # si le répertoire existe, on demande si on doit l'écraser
    if [ -d $module ]
    then
	echo "Le répertoire existe déjà"
    else
	# Création
	mkdir $module

	echo $filePattern > $fichier
	echo "" > "${module}/__init__.py"

	# Création fichiers supplémentaires
	for i in $@
	do
	    # pour chaque arguement dont le nom est != du module
	    if [[ $i != $module ]]
	    then
		echo $filePattern > "${module}/$i"
	    fi
	done
    fi
    # tous les fichiers ont été créés... Ou non.
fi
    



