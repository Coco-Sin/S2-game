# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

# external plug-in
import sys

e = None

### on crée une fonction help qui pourra aider le joueur tout au long du jeu
def Create(helpme):
	help = dict()
	myfile_2 = open(helpme, "r")
	help["str"] = myfile_2.read()
	myfile_2.close()
	return help
	
### on affiche par dessus la carte une nouvelle fenêtre HelpME qui retournera les aides en fonction du numéro de l'énigme choisie
def HelpME():

    global e
    sys.stdout.write("\033[1;1H")    ### on efface la fenêtre de la carte principale pour afficher celle de help
    sys.stdout.write("\033[2J")
	
	# indications
    txt = "Tu trouveras ton aide ici-meme"
    sys.stdout.write(txt)
	
    txt = "\nNuméro de l'énigme ?"
    sys.stdout.write(txt)

    nume = raw_input()

    # aides selon les différentes énigmes

    if nume == "2" :
        e = "Une formule pourrait vous être utile... Rappelez-vous : d = v x t"
        
    elif nume == "3":
        e = "On aura besoin des 3 nombres de la classe des millions, ensuite vous pouvez utiliser une calculatrice :)"
       
    elif nume == "4" :
        e = "Commencer par poser les choses simplement : 4x = (130-x)/3...bonne résolution !" 
             
    elif nume == "5" :
        e = "Commencer par poser les choses simplement : 1/2x = 3/4 * (12-x). \n Ne reste plus qu'à résoudre et convertir en heure et minutes ;)"  
          
    elif nume == "1" or nume == "6" :
        e = "Tu n'en as pas vraiment besoin ici ;) Réessaye avec une autre touche si tu t'es trompé :)"
    
    elif nume == "7" :
        e = "Tu peux t'aider d'internet, je pense notamment pour la 5ème question. \n Pour ce qui est du reste tu devrait t'en sortir ;)"
    
    elif nume == "8" :
        e = "Utilise la référence ~ Déclaration des droits de l’homme et du citoyen (26 août 1789) ~ dans Encyclopédie puis Politique \n (PS : il faudra compter le nombre de mots pour déceler le message codé)"

    else :
        e = "ce n'est pas une lettre valide, veuillez réessayer"
         
    return e

# règle l'affichage de help
def show(help):
    
	sys.stdout.write("\033[1;1H")
	
	txt = "Tu trouveras ton aide ici-meme \n PS : Vous pouvez rappuyez sur h et rentrer à nouveau votre réponse afin d'éviter de retourner sur la map ;)"
	sys.stdout.write(txt)
	
	sys.stdout.write("\033[37m")
	
	sys.stdout.write("\033[40m")
	
	sys.stdout.write(help["str"])
        sys.stdout.write("\0")

        print e
           
	return







