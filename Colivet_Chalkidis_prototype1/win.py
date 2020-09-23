# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

import sys
import interactEnigmes
import Enigma


### création de l'écran victoire
def create(vic):
	victoire = dict()
	myfile_1 = open(vic, "r")
	victoire["str"] = myfile_1.read()
	myfile_1.close()
	return victoire
	
### affichage de la victoire	
def show(victoire):
	

	sys.stdout.write("\033[1;1H")


	sys.stdout.write("\033[37m")
	
	sys.stdout.write("\033[40m")
	
	sys.stdout.write(victoire["str"])
        sys.stdout.write("\0")


	return




