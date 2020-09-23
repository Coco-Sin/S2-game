# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

# external plug-in
import sys
import os
import select
import tty
import termios
import time

# my plug-in
import Background
import Enigma
import Help
import interactEnigmes
import Player
import Introduction
import grille
import win
import Information


MyPlayer = None
myBackground = None
timeStep = None
Affichage = "intro"
MyHelp = None
Ex1 = None
Ey1 = None
MyIntro = None
MyGrid = None
MyVictoire = None
MyInfo = None

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

### initialisation des différents paramètres
def init():
    global MyPlayer, myBackground, timeStep, MyHelp, MyIntro, MyGrid, MyInfo
	
    #initialisation de la partie
    timeStep=0.2
	
    MyPlayer = Player.createPlayer(color=5,
                x=2,
                y=3,
                xMax=90,
                yMax=25,
                speed=4, 
                direction = None)
    myBackground = Background.create("image.txt")
    MyHelp = Help.Create("Help.txt")
    MyIntro = Introduction.create("message_intro.txt")
    MyGrid = grille.create("grille_mots_croises_jeu.txt")
    MyInfo = Information.Create("information.txt")

    tty.setcbreak(fd)
    return

### définition du déplacement de l'animat
def move():
    global MyPlayer,myBackground,Player,Background, Ex1, Ey1
    #deplacement animat-

    if 1<int(MyPlayer['y'])<26:
      x,y=Player.getNextPosition(0.2,MyPlayer)               #On recupere la prosition suivante de l'animat
      if (Background.GetCaractere(myBackground,x,y)==" ") :  #On change le background si la position suivante est un espace sinon arret de l'animat
          Player.move(0.2,MyPlayer)

      elif (Background.GetCaractere(myBackground,x,y) == "X"):
          x = int(x)
          y = int(y)
          valeur = (x,y)
          sys.stderr.write(str(valeur))
          MyPlayer["direction"] = None 
          if (x,y) == (14,5):
              interactEnigmes.Enigme1()
          elif (x,y) == (45,3):
              interactEnigmes.Enigme2()
          elif (x,y) == (64,5):
              interactEnigmes.Enigme3()
          elif (x,y) == (51,17):
              interactEnigmes.Enigme4()
          elif (x,y) == (47, 20):
              interactEnigmes.Enigme5()
          elif (x,y) == (8,16):
              interactEnigmes.Enigme6()
          elif (x,y) == (19,26):
              interactEnigmes.Enigme7()
                
    else:
      Player.move(0.2,MyPlayer)

    return

### intéractions possibles pour le joueur pour accéder à son Notebook, la carte, les aides ou pour se déplacer
def interact():
    global Player, Background, Help, Affichage, grille, Information
    if isDataReady():
	c = sys.stdin.read(1)
        if c == '\x1b':
            QuitGame()
        elif c == 'm':
	    Affichage = "back"
        elif c == 'h':
	    Affichage = "hlp"
            Help.HelpME()
        elif c == 'z':
	    Player.MoveForward(MyPlayer)
        elif c == 's':
	    Player.MoveBackward(MyPlayer)
        elif c == 'd':
	    Player.MoveRight(MyPlayer)
        elif c == 'q':
	    Player.MoveLeft(MyPlayer)
        elif c == 'g':
            Affichage = "grd"
        elif c == 'i':
            Affichage = "info"
	
    return Affichage

### affichage du backgroud, de l'animat, du notebook et du menu help
def show():
    global Background, Player, Affichage, e, interactEnigmes, Information

	
    sys.stdout.write("\033[2J")


    if Affichage == "back":
        Background.show(myBackground)
        Player.show(MyPlayer)

    elif Affichage == "hlp":
        Help.show(MyHelp)

    elif Affichage == "intro":
        Introduction.show(MyIntro)

    elif Affichage == "grd":
        grille.show(MyGrid)

    elif Affichage == "info":
        Information.show(MyInfo)
       
    sys.stdout.write("\033[37m")
	
    sys.stdout.write("\033[40m")
	
    sys.stdout.write("\033[0;0H\n")
	
    return


def isDataReady(): 
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def run():
    global timeStep
	
    while 1: 
        interact()
        move()
        show()
        time.sleep(timeStep)
    return
	

### fin du jeu
def QuitGame():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
	
    sys.stdout.write("\033[37m")
	
    sys.stdout.write("\033[40m")
	
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    sys.exit()
    return
	
	
if __name__ == "__main__" :
    init()
    run()
    QuitGame()
		
