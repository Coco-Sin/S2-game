# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

import sys
import interactEnigmes
import Enigma



def create(los):
	defaite = dict()
	myfile_1 = open(los, "r")
	defaite["str"] = myfile_1.read()
	myfile_1.close()
	return defaite
	
### affichage de la defaite	
def show(defaite):
	
        sys.stderr.write(str(defaite))
	sys.stdout.write("\033[1;1H")


	sys.stdout.write("\033[37m")
	
	sys.stdout.write("\033[40m")
	
	sys.stdout.write(defaite["str"])
        sys.stdout.write("\0")


	return




