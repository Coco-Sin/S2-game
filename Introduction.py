# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

import sys
            
def create(introduc):
	introduction = dict()
	myfile_1 = open(introduc, "r")
	introduction["str"] = myfile_1.read()
	myfile_1.close()
	return introduction
	
### affichage de l'intro	
def show(introduction):
	

	sys.stdout.write("\033[1;1H")
 

	sys.stdout.write("\033[37m")
	
	sys.stdout.write("\033[40m")
	
	sys.stdout.write(introduction["str"])
        sys.stdout.write("\0")


	return

