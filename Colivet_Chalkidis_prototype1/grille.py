# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

import sys

### création de la grille 
def create(grd):
	grille = dict()
	myfile_1 = open(grd, "r")
	grille["str"] = myfile_1.read()
	myfile_1.close()
	return grille
	
### affichage de la grille	
def show(grille):

	sys.stdout.write("\033[1;1H")

	sys.stdout.write("\033[37m")
	
	sys.stdout.write("\033[40m")
	
	sys.stdout.write(grille["str"])
        sys.stdout.write("\0")


	return

