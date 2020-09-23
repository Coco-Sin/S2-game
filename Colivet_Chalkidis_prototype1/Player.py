# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

import sys

"""
Création de MyPlayer
"""

### création de myPlayer ou animat
def createPlayer(color,x,y,xMax,yMax,speed,direction):
    MyPlayer = dict()
    MyPlayer["color"] = color
    MyPlayer["x"] = x
    MyPlayer["y"] = y
    MyPlayer["xMax"] = xMax
    MyPlayer["yMax"] = yMax
    MyPlayer["speed"]= speed
    MyPlayer["direction"]= direction
    return MyPlayer

"""
Affichage de MyPlayer
"""

def show(a):
    x = str(int(a["x"]+1))
    y = str(int(a["y"]+1))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)
	
    #couleur de fond
    sys.stdout.write(txt)
	
    #couleur MyPlayer
    c = a["color"]
    txt = "\033[3"+str(c%7+1) + "m"
    sys.stdout.write(txt)
	
    #affichage de MyPlayer
    caractere = "§"
    sys.stdout.write(caractere)
    return

#position de l'animat
def getNextPosition(dt,a):
    x=a['x']
    y=a['y']
    if a["direction"]=="forward":
        y=(a["y"]-(a["speed"]*dt))      
    elif a["direction"]=="right":
        x=(a["x"]+(a["speed"]*dt))
    elif a["direction"]=="backward":
        y=(a["y"]+(a["speed"]*dt))
    elif a["direction"]=="left":
        x=(a["x"]-(a["speed"]*dt))
    return x,y

"""
Mouvements de MyPlayer
"""

def move(dt,a):
    x, y = getNextPosition(dt,a)
    a["x"] = x
    a["y"] = y

    '''
    if a["direction"]=="forward":
        a["y"]=(a["y"]-(a["speed"]*dt))%a["yMax"] 
    elif a["direction"]=="right":
        a["x"]=(a["x"]+(a["speed"]*dt))%a["xMax"]
    elif a["direction"]=="backward":
        a["y"]=(a["y"]+(a["speed"]*dt))%a["yMax"]
    elif a["direction"]=="left":
        a["x"]=(a["x"]-(a["speed"]*dt))%a["xMax"]
    '''
    return

def MoveRight(a):
    a["direction"] = "right"
    return
	
def MoveLeft(a):
    a["direction"] = "left"
    return
	
def MoveForward(a):
    a["direction"] = "forward"
    return
	
def MoveBackward(a):
    a["direction"] = "backward"
    return
