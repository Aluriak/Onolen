CC=python


all:
	$(CC) main.py

clean:
	# Nettoyage complet
	rm -r *.pyc
	rm -r */*.pyc
	rm -r */*/*.pyc
	rm erreur.txt

cleanlogs:
	# Nettoyage des logs
	rm log
