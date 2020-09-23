# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

# externaal plug-in
import sys

"""
ce module permet de changer les emplacements, d'afficher la carte et le caractère (répuration des valeurs)
"""

def create(filename):
    background = dict()
    myfile = open(filename, "r")
    background["str"] = myfile.read()
    myfile.close()
    background['caractere'] = background["str"].split('\n')
    return background

# récupérer l'affichage du caractère et de la carte
def GetCaractere(background,x,y):
    c = background['caractere'][int(y)][int(x)]
    return c


# afficher la carte principale 
def show(background):
	
    sys.stdout.write("\033[1;1H")
	
	# affichage du texte au dessus de la carte de jeu
    txt = "Bienvenue dans ce super jeu ! C'est un escape game. Tu vas devoir résoudre des enigmes afin de sortir d'une pièce où tu seras emprisonné."
    sys.stdout.write(txt)
	
    txt = " Je te souhaite bon courage et bon jeu !"
    sys.stdout.write(txt)
	
	
    sys.stdout.write("\033[37m")
	
    sys.stdout.write("\033[40m")
	
    sys.stdout.write(background["str"])
	
    return
	

