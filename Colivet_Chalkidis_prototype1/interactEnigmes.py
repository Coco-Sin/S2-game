# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################


import sys
import Enigma
import Main
import win



### coin bureau et astronomie

### définition du menu desk1
def Enigme1():

  ### affichage du menu
  sys.stdout.write("\033[1;1H")      ### on supprime la carte pour afficher le menu du bureau 1
  sys.stdout.write("\033[2J")

  txt = "appuyer sur m tout au long de votre exploration pour revenir sur le jeu\n"
  sys.stdout.write(txt)

  print "Vous êtes face à un bureau, c'est une table sur laquelle on peut écrire, travailler, enfermer des papiers et faire encore plus de choses trop cool !"
  menudesk1 = "\nQue voulez-vous faire ? (entrez la lettre correspondante)\n" 
  sys.stdout.write(menudesk1)

### différentes possibilités s'offrent à vous
  pa = u" a.  Feuilleter le carnet de notes"
  print pa
    
  pb = u" b.	Examiner la boîte cadenassée "
  print pb
     
  pc = u" c.	Jeter un coup d’œil aux feuilles"
  print pc

  pd = u" d.	Examiner le télescope"
  print pd

  pe = u" e.	Revenir à la carte principale "
  print pe

  ### menu du bureau 1
  while 1:
    test1 = raw_input()

    # possibilité a
    if test1 == "a":
        carnetperso = u"A. Le carnet est presque vide… Il y a quelque chose d’écrit au tout début"
        print carnetperso
        
        # x1 prend la valeur renvoyée par l'énigme 1 dans le module enigma
        x1 = Enigma.enigma1() 
        sys.stdout.write(x1)
        #Notebook.append(x1)
        
    # possibilité b
    elif test1 == "b":
        x3 = Enigma.enigma3()
        sys.stdout.write(x3)

        #### vérification et récupération de l'indice
        verif3 = u"\n Entrez le code obtenu pour obtenir l'indice"
        r3 = 621
        if r3 == input(verif3) :
            juste3 = u"\n \n Tient une clef en argent avec Shandra gravé dessus !  Je me demande à quoi elle va bien pouvoir me servir… \n Tient c’est étrange, on a récupéré un morceau de papier avec indiqué : 14/23/12/8/12/21/24/25/14/13/18/14 , 22/10/3/17/2 , C = 12"
            print juste3

            #Notebook.append("clef en argent")

        else :
            faux3 = u"\n Non, réessayer \n si vous avez besoin d'aide appuyer sur la touche h une fois sorti de l'énigme et entrez le numéro de l'énigme"
            print faux3
    
    # possibilité c
    elif test1 == "c":
        x2 = Enigma.enigma2()
        sys.stdout.write(x2)
        verif2 = u"\nVeuillez entrer votre réponse pour vérification"
        print verif2

        # vérification
        r2 = 180000000
        if r2 == int(raw_input()) :
            #Notebook.append(r2)
            juste2 = u"\n \n Bonne réponse ! N'oubliez pas de prendre en note vos résultats pour chaque énigme !"
            print juste2

        else :
            faux2 = u"\n Non, recommencez \n i vous avez besoin d'aide appuyer sur la touche h et entrez le numéro de l'énigme"
            print faux2
    
    # possibilité d
    elif test1 == "d":
        telescope = u"\n \n Il n’y a rien de particulier ici… il semblerait qu’il appartenait à Isaac Newton"
        print telescope

    ### retourner à la carte principale
    elif test1 == "e" or test1 == "m":
        return
    
    # si on met une lettre différente de celles proposées
    else:
      print u"\n ce n'est pas une lettre valide, veuillez réessayer"

### coin bibliothèque

# munu objet bibliothèque 
def Enigme2():

  # affichage du menu de la bibliothèque 
  sys.stdout.write("\033[1;1H")
  sys.stdout.write("\033[2J")

  txt = "appuyer sur m tout au long de votre exploration pour revenir sur le jeu\n"
  sys.stdout.write(txt)

  print "Vous êtes face à une bibliothèque, il y a beaucoup de livres"
  menulibrary = "\nQue voulez-vous faire ? (entrez la lettre correspondante)\n" 
  sys.stdout.write(menulibrary)

  ### différentes possibilités s'offrent à vous
  pa = u"a.  Examiner l’étagère "
  print pa
    
  pb = u"b.  Revenir à la carte principale "
  print pb
  
  ### menu de l'objet bibliothèque
  while 1:
    test1 = raw_input()
    if test1 == "a":


        # possibilité A dans a
        pA = u"A. Diderot et d’Alembert"
        print pA

        pB = u"B. Montesquieu"
        print pB

        pC = u"C. Rousseau"
        print pC

        pD = u"D. Voltaire"
        print pD

        pE = u"E. Revenir carte"
        print pE

        test2 = raw_input()

        if test2 == "A" or test2 == "a" : #Alembert
            pi = u"i.   Mathématiques"
            print pi

            pii = u"ii. Sortir d'ici"
            print pii
 
            test3 = raw_input()
            if test3 == "i":
                x4 = Enigma.enigma4()
                sys.stdout.write(x4)
                verif4 = u"veuillez entrer vos réponses (peut importe l'odre des deux nombres)"
                print verif4
                
                print "\n entrez votre premier nombre:"
                test4 = int(raw_input())

                if test4 == 10:
                    print "\n Votre premier nombre est bon"
                    print "\n Entrez votre deuxieme nombre:"
                    test5 = int(raw_input())
                    if test5 == 120:
                        print "Bonne réponse !"
                    elif test5 == "m":
                        return
                    else:
                        print "\n Ce n'est pas le bon nombre ou alors ce n'est pas un nombre, veuillez reessayer"


                elif test4 == 120:
                    print "\n Votre premier nombre est bon"
                    print "\n Entrez votre deuxieme nombre:"
                    test5 = int(raw_input())
                    if test5 == 10:
                        print "\n Bonne réponse ! Conservez bien ces nombres et le numéro de l'énigme !!"
                    elif test5 == "m":
                        return
                    else:
                        print "\n Ce n'est pas le bon nombre ou alors ce n'est pas un nombre, veuillez reessayer"
                
                ### retourner à la carte principale
                elif test4 == "m":
                    return
                
                ### si on met une lettre différente de celles proposées
                else:
                    print "\n Ce n'est pas le bon nombre ou alors ce n'est pas un nombre, veuillez reessayer"

            ### retourner à la carte principale    
            elif test3 =="ii" or test3 == "m":
                return
            
            ### si on met une lettre différente de celles proposées
            else:
                print u"\n \n ce n'est pas une lettre valide, veuillez réessayer"
             
        # possibilité B dans a 
        elif test2 =="B" or test2 == "b" : 
            montesquieu = u"Montesquieu, Lettres persanes (1721), 24 (extrait) \n Ne crois pas que je puisse, quant à présent, te parler à fond des mœurs et \n des coutumes européennes : je n’en ai moi-même qu’une légère idée, et je \n n’ai eu à peine que le temps de m’étonner. Le roi de France est le plus \n puissant prince de l’Europe. Il n’a point de mines d’or comme le roi \n d’Espagne, son voisin ; mais il a plus de richesses que lui, parce qu’il les \n tire de la vanité de ses sujets, plus inépuisable que les mines. On lui a vu \n entreprendre ou soutenir de grandes guerres, n’ayant d’autres fonds que \n des titres d’honneur à vendre, et, par un prodige de l’orgueil humain, ses \n troupes se trouvaient payées, ses placesa munies, et ses flottes équipées.\n D’ailleurs ce roi est un grand magicien : il exerce son empire sur l’esprit \n même de ses sujets ; il les fait penser comme il veut. S’il n’a qu’un million \n d’écus dans son trésor, et qu’il en ait besoin de deux, il n’a qu’à leur \n persuader qu’un écu en vaut deux, et ils le croient. S’il a une guerre difficile \n à soutenir, et qu’il n’ait point d’argent, il n’a qu’à leur mettre dans la tête \n qu’un morceau de papier est de l’argent, et ils en sont aussitôt convaincus. \n Il va même jusqu’à leur faire croire qu’il les guérit de toutes sortes de maux \n en les touchant, tant est grande la force et la puissance qu’il a sur les esprits."

            print montesquieu
        
        # possibilité C dans a
        elif test2 =="C" or test2 == "c" :
            rousseau = u"Jean-Jacques Rousseau, Julie ou La Nouvelle Héloïse (1761), 6e partie, Lettre VIII \n Tant qu’on désire on peut se passer d’être heureux ; on s’attend à le devenir : \n si le bonheur ne vient point, l’espoir se prolonge, et le charme de l’illusion dure \n autant que la passion qui le cause. Ainsi cet état se suffit à lui-même, et \n l’inquiétude qu’il donne est une sorte de jouissance qui supplée à la réalité, qui \n vaut mieux peut-être. Malheur à qui n’a plus rien à désirer ! Il perd pour ainsi \n dire tout ce qu’il possède. On jouit moins de ce qu’on obtient que de ce qu’on \n espère et l’on n’est heureux qu’avant d’être heureux. En effet, l’homme, avide \n et borné, fait pour tout vouloir et peu obtenir, a reçu du ciel une force consolante \n qui rapproche de lui tout ce qu’il désire, qui le soumet à son imagination, qui le \n lui rend présent et sensible, qui le lui livre en quelque sorte, et, pour lui rendre \n cette imaginaire propriété plus douce, le modifie au gré de sa passion. Mais tout \n ce prestige disparaît devant l’objet même ; rien n’embellit plus cet objet aux \n yeux du possesseur ; on ne se figure point ce qu’on voit ; l’imagination ne pare \n plus rien de ce qu’on possède, l’illusion cesse où commence la jouissance. Le \n pays des chimères est en ce monde le seul digne d’être habité, et tel est le néant \n des choses humaines, qu’hors l’Etre existant par lui-même il n’y a rien de beau \n que ce qui n’est pas. Si cet effet n’a pas toujours lieu sur les objets particuliers \n de nos passions, il est infaillible dans le sentiment commun qui les comprend \n toutes. Vivre sans peine n’est pas un état d’homme ; vivre ainsi c’est être mort. \n Celui qui pourrait tout sans être Dieu serait une misérable créature ; il serait \n privé du plaisir de désirer ; toute autre privation serait plus supportable.."
            print rousseau

        # possibilité D dans a
        elif test2 =="D" or test2 == "d":
            voltaire = u"Voltaire, Dictionnaire philosophique (1764), article ~ Torture (extrait) \n Lorsque le chevalier de La Barre, petit-fils d’un lieutenant-général des \n armées, jeune homme de beaucoup d’esprit et d’une grande espérance, \n mais ayant toute l’étourderie d’une jeunesse effrénée, fut convaincu \n d’avoir chanté des chansons impiesc, et même d’avoir passé devant une \n procession de capucins sans avoir ôté son chapeau, les juges \n d’Abbeville, gens comparables aux sénateurs romains, ordonnèrent, non \n seulement qu’on lui arrachât la langue, qu’on coupât la main, et qu’on \n brûlât son corps à petit feu ; mais ils l’appliquèrent encore à la torture \n pour savoir précisément combien de chansons il avait chantées, et \n combien de processions il avait vues passer, le chapeau sur la tête. Ce \n n’est pas dans le XIIIe ou dans le XIVe siècle que cette aventure est \n arrivée, c’est dans le XVIIIe. Les nations étrangères jugent de la France \n par les spectacles, par les romans, par les jolis vers, par les filles \n d’Opéra, qui ont les mœurs fort douces, par nos danseurs d’Opéra, qui \n ont de la grâce, par Mlle Clairon , qui déclame des vers à ravir. Elles ne \n savent pas qu’il n’y a point au fond de nation plus cruelle que la française."
            print voltaire
            
        # possibilité E dans a
        elif test2 == "e" or test1 == "m":
            return
        
        ### si on met une lettre différente de celles proposées
        else:
            print u"\n ce n'est pas une lettre valide, veuillez réessayer"
      
    # possibilité dans b ~ retourner à la carte principale
    elif test1 == "b" or test1 == "m":
        return

    ### si on met une lettre différente de celles proposées
    else:
        print u"\n ce n'est pas une lettre valide, veuillez réessayer"
      
    
### menu de l'objet sofa
def Enigme3():

  ### affichage du menu canapé
  sys.stdout.write("\033[1;1H")
  sys.stdout.write("\033[2J")

  txt = "appuyer sur m tout au long de votre exploration pour revenir sur le jeu\n"
  sys.stdout.write(txt)

  print "Vous êtes face à un bon canapé en cuir qui a l'air très confortable"
  menusofa = "\nQue voulez-vous faire ? (entrez la lettre correspondante)\n" 
  sys.stdout.write(menusofa)

  ### différentes possibilités s'offrent à vous
  pa = u"a. Soulever les cousins"
  print pa

  pb = u"b. S'assoir sur le canapé"
  print pb

  pc = u"c. Revenir à la carte principale"
  print pc

  # menu de l'objet canapé
  while 1:
      testcanap = raw_input()

      # possibilité a
      if testcanap == "a":
          print u"Il n'y a rien ici"
      
      # possibilité b 
      elif testcanap =="b":
          print u"le temps passe ......."
          print u" Faudrait peut-être avancer un jour"
     
      # possibilité c ~ retourner à la carte principale
      elif testcanap =="c" or testcanap == "m" :
          return
      
      ### si on met une lettre différente de celles proposées
      else:
          print u"ce n'est pas une lettre valide, veuillez réessayer"

### coin salon culturel


def Enigme4():

  ### affichage du menu feuilles
  sys.stdout.write("\033[1;1H")
  sys.stdout.write("\033[2J")

  txt = "appuyer sur m tout au long de votre exploration pour revenir sur le jeu\n"
  sys.stdout.write(txt)
  print "Vous êtes face à une paquet de feuille par terre\n"
  menusheet = "Que voulez-vous faire ? (entrez la lettre correspondante)\n"
  sys.stdout.write(menusheet)

  ### différentes possibilités s'offrent à vous
  pa = u"a. Y jeter un coup d'oeil"
  print pa

  pb = u"b. Revenir à la carte"
  print pb

  while 1:
      testsheet = raw_input()
      # possibilité a
      if testsheet == "a":
          x7 = Enigma.clue1()
          sys.stdout.write(x7)

          print "Vous avez maintenant découvert qu'en appuyant sur G, \n vous pouvez avoir accès tout le temps à cette grille"
      
      # possibilité b ~ retourner à la carte principale
      elif testsheet =="b" or testsheet == "m" :
          return
      
      ### si on met une lettre différente de celles proposées
      else:
          print u"\n ce n'est pas une lettre valide, veuillez réessayer"



# menu de l'objet petite armoire
def Enigme5 () :
    
    ### affichage du menu petite armoire
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    txt = "appuyer sur m tout au long de votre exploration pour revenir sur le jeu"
    sys.stdout.write(txt)

    menuarmoire = "\nQue voulez-vous faire ? (entrez la lettre correspondante)\n" 
    sys.stdout.write(menuarmoire)
    
    ### différentes possibilités s'offrent à vous
    pa = u"a. Ouvrir le premier"
    print pa

    pb = u"b. Ouvrir le second tiroir"
    print pb

    pc = u"c. Revenir à la carte"
    print pc

    # menu de l'objet petite armoire
    while 1 :
        answer = raw_input()
        
        # possibilité a
        if answer == "a" :
            carnet = u"A. Il y a un carnet verrouillé... Il semblerait qu’on est besoin d'une clef ou plutôt d'un prénom... \n Veuillez entrer votre réponse"
            print carnet

            ### vérification
            reponse = "Shandra"
            if reponse == raw_input():
                x9 = Enigma.clue3()
                sys.stdout.write(x9)
                
            
            ### si on met une lettre différente de celles proposées
            else : 
                faux = u"\n ce n'est pas le bon prénom, veuillez réessayer"
                print faux
        
        # possibilité b
        elif answer == "b" :
            x8 = Enigma.clue2()
            sys.stdout.write(x8)
            
        
        # possibilité c ~ retourner à la carte principale
        elif answer == "c" or answer == "m" :
            return
        
        ### si on met une lettre différente de celles proposées
        else :
            print u"\n ce n'est pas une lettre valide, veuillez réessayer"


### coin mathématiques et naviguation

### menu de l'objet desk2
def Enigme6() :

    ### affichage du menu bureau 2
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    txt = "appuyer sur m tout au long de votre exploration pour revenir sur le jeu"
    sys.stdout.write(txt)

    menudesk2 = "\nQue voulez-vous faire ? (entrez la lettre correspondante)\n" 
    sys.stdout.write(menudesk2)

    ### différentes possibilités s'offrent à vous
    pa = u"a.   Consulter les feuilles de calculs"
    print pa

    pb = u"b.   Retourner à la carte principale"
    print pb

    ### menu de l'objet bureau 2
    while 1 :
        answer = raw_input()
        if answer == "a" :
            x5 = Enigma.enigma5()
            sys.stdout.write(x5)

            ### vérification et récupération de l'indice
            verif5 = u"\n Veuillez entrer votre réponse pour vérification, vous ecrirez sous la forme ..h.."
            print verif5
            r5 = raw_input()

            # si juste
            if r5 == "7h12" :
                juste5 = u"\n \n Bien joué ! Par la suite vous ne garderez que le nombre 712"
                print juste5
                

            # si faux
            else :
                faux5 = u"\n Non réessayer, vous pouvez y arriver !!! \n si vous avez besoin d'aide appuyer sur la touche h (une fois sorti de l'énigme) et entrez le numéro de l'énigme"
                print faux5
        
        # retourner à la carte principale
        elif answer == "b" or answer == "m" :
            return
        
        ### si on met une lettre différente de celles proposées
        else :
            print u"\n ce n'est pas une lettre valide, veuillez réessayer"


def Enigme7() :
    global Affichage
    ### affichage du menu de fin
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    text = "1. De la réponse de l’énigme 2, prendre les 3 chiffres de la classe des millions et le doubler. \n 2. Prendre le résultat de l’énigme 3 et l’additionner au résultat précédent \n 3. Soustraire le résultat de l’énigme 4 au nombre obtenu précedemment \n 4. Prendre le nombre de lettres dans la réponse de l’indice 2 et le multiplier au résultat trouvé précédemment \n 5. Soustraire la valeur trouvée dans l’indice 3 au résultat en cours \n Maintenant, compliquons les choses... il va vous falloir penser simplement...\n 6. Remettre les chiffres dans l’ordre décroissant : vous obtenez un nombre. \n Diviser le par le nombre pair dont le nombre de diviseurs est égal à ma valeur moins une unité (ne garder que le nombre entier du résultat obtenu) \n 7. L’additionner avec le nombre obtenu à l’énigme 5 \n On obtient ?"
    print text
    print "\n \n Entrez 12 si vous voulez sortir"

    while 1:
        rf = int(raw_input())
        if rf == 3167 :
            sys.stdout.write("\033[1;1H")
            sys.stdout.write("\033[2J")
            MyVictoire = win.create("win.txt")
            win.show(MyVictoire)
        elif rf == 12:
            return
        else:
            print u"\n Non veuillez réessayer, vous y êtes presque !"

