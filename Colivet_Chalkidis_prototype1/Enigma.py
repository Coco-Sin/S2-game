# -*- coding: utf-8 -*-
#########################
# main.py               #
# E.Chalkidis_C.Colivet #
# S2P-A-01        2020  # 
#########################

# définition des énigmes à appeler dans le menu interact.Enigmes.py

# énigme 1 ~ objet : le carnet de notes de Léonard de Vinci
def enigma1() :
	text1 = "Enigme 1 \n Il y a quelque chose d'indiqué dessus... \n La distance éloignant l'étoile du berger du soleil permettra d'accéder à la clef..."
	return text1

# énigme 2 ~ objet : feuilles avec des formules
def enigma2() :
	text2 = "Enigme 2 \n La lumière met 0,1 heure pour nous parvenir, sachant que la lumière du Soleil met environ 300.000 km par secondes pour nous parvenir... \n La distance trouvée sera un nombre entier en kilomètres"
	# réponse : 180 000 000 km
	return text2

# énigme 3 ~ objet : une boîte cadenassée 
def enigma3() :
	text3 = "Enigme 3 \n Dans la classe des millions il me faudra le chiffre des centaines, des dizaines et de l’unité. En les additionnant un à un on obtient un nombre X. \n En l’élevant au cube et en soustrayant le nombre de départ à ce nombre, on obtient le code final. "
	# réponse : 621
	return text3

# énigme 4 ~ objet : dans l'encyclopédie, tome Mathématiques
def enigma4() :
	text4 = "Enigme 4 \n Les enfants ont 130 noisettes et doivent les diviser en deux tas, de sorte que le quadruple du plus petit tas soit égal au tiers du plus gros tas. \n Combien doivent-ils mettre de noisettes dans chaque tas ? "
	# réponse 120 et 10
	return text4

# énigme 5 ~ objet : feuilles de calculs disposées sur le bureau
def enigma5() :
	text5 = "Enigme 5 \n Question à poser à Mademoiselle Émilie du Châtelet : La moitié du temps écoulé depuis minuit est égal aux trois quarts du temps qu’il ne reste avant midi. \n Quelle heure est-il ? (donner la réponse sous la forme (...h...)"
	# réponse : 7h12(A.M.) 
	return text5


#######################################################################################
# défintion des indices à appeler dans le menu interact.Enigmes.py

# indice 1 ~ objet : morceau de papier par terre
def clue1() :
	text7 = "Indice 1 \n Voyons voir... un morceau de papier avec une grille vide à compléter... Ne reste plus qu'à trouver les questions ! "
	return text7

# indice 2 ~ objet : tiroir
def clue2() :
	text8 = "Indice 2 \n Tient un papier avec des questions ! \n ... Q1/ Je suis un savant polonais ayant découvert, au XVIème siècle, que la Terre n’était pas le centre de l’univers (notion d'héliocentrisme). \n Q2/ Je suis un chant patriotique de la Révolution Française composé par Rouget de Lisle ? \n Q3/ Comment appelle-t-on le bonnet rouge porté par les révolutionnaires français ? \n Q4/ Quel auteur français a dénoncé les injustices sociales au XVIIIème siècle : Bernard-Henri Lévy, Voltaire ou Pascal ? \n Q5/ Dans le salon de quelle figure féminine célèbre c’est tenu la lecture de la tragédie de « L’orphelin en Chine » de Voltaire ? (ne garder que le nom de famille) \n Q6/ Je suis l’auteur de la nouvelle Héloïse, je suis également un philosophe important du siècle des Lumières. Qui suis-je ? \n Q7/ Quelle célèbre déclaration a été votée le 26 août 1789 par les députés français ? (on ne demandera que les initiales)\n Mon tout est le symbole des Lumières, des connaissances récoltées, discuté dans les salons culturels et diffusé à travers le monde grâce à l'imprimerie"                   
	# réponse 1 : Copernic
	# réponse 2 : Marseillaise
	# réponse 3 : bonnet phrygien
	# réponse 4 : Voltaire
	# réponse 5 : Le salon de Madame Geoffrin (Geoffrin)
    # réponse 6 : Rousseau
    # réponse 7 : Déclaration des droits de l’Homme et du citoyen (DDHC)
	# L'ENCYCLOPEDIE
	return text8

# indice 3 ~ article de journaux
def clue3() :
	text9 = "Indice 3 \n la réponse à l'indice 2 + POLITIQUE sera la référence \n Code /m.41/ /m.36/ boite et /m.32/ enlever chiffre des /m.61/ récupérer code. Ne garder que les 3 premiers chiffres"
	# réponse : 432
	return text9
	