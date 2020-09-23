# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

# external plug-in
import sys

# My plug-in
import timerEG

### on crée une fonction information qui pourra informer le joueur sur le temps restant et les règles du jeux (récapitulatif)
def Create(information) :
	info = dict()
	myfile_3 = open(information, "r")
	info["str"] = myfile_3.read()
	myfile_3.close()
	return info


### réglage de l'affichage de information
def show(info) :
        
	sys.stdout.write("\033[1;1H")
	
	# indications
	txt = " Tu trouveras les informations utiles ici même "
	sys.stdout.write(txt)
	
        txt = " Le but du jeu et de réunir tout les indices pour pouvoir sortir de la pièce dans le temps imparti (voir le minuteur ci-dessous) \n Pour se faire vous devez rentrer en contact avec les objets représentés par des X pour accéder à leur menu. \n En explorant les menus vous pourrez peut être trouver des énigmes voir des indices...\n En cas de soucis, n'hésitez pas à accéder aux aides en appuyant sur la touche h... \n Bonne chance à vous! "
        sys.stdout.write(txt)

        txt = "\n z permet de se déplacer vers le haut \n q permet de se déplacer vers la gauche \n s permet de se déplacer vers le bas \n d permet de se déplacer vers la droite \n h permet d’accéder à l’aide associée à l’énigme en cours \n m permet de retourner à la carte principale \n i permet d'accéder aux informations ici présentes\n"
        sys.stdout.write(txt)

	sys.stdout.write("\033[37m")
	
	sys.stdout.write("\033[40m")
	
	sys.stdout.write(info["str"])
        sys.stdout.write("\0")

        return






