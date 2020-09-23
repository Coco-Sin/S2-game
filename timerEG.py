# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

# external plug-ins
import time


# création du dictionnaire time 
def create(nb_sec, timeIni) :
	minuteur = dict()
	minuteur["timeTemp"] = timeIni
	minuteur["actualTime"] = nb_sec


	return minuteur


# définition du minuteur
def minuteur(timer):
        now = time.time()
	temps = now - timer["timeTemp"]  
	timer["actualTime"] = timer["actualTime"] - temps
	timer["timeTemp"] = now



# affichage du minuteur
def showMinuteur(minuteur):
	q,s = divmod(minuteur,60)
	h,m = divmod(q,60)
	return "%d:%d:%d > %d" %(h,m,s,minuteur)



