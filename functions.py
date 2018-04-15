"""
    Cet module contiendra toutes les fonctions dont nous aurons besoin
"""
#------------------------------------------------------------
# @author Aboubacar Ouattara
# @copyright All rights reserved
#------------------------------------------------------------
from colored import fg,bg,attr
import os

#------------------------------------------------------------
#   Cette fonction permet d'afficher un message avec couleur
#------------------------------------------------------------

def printMessage(message,color="white",background=0,reset=0):
    if background != 0:
        print("%s%s %s %s" %(fg(color), bg(background), message,attr(reset)))
    else:
        print("%s %s %s" %(fg(color), message,attr(reset)))
#------------------------------------------------------------
#   Cette fonction permet de nettoyer le terminal
#------------------------------------------------------------

def clearTerminal():
    os.system("cls" if os.name=="nt" else "clear")

#------------------------------------------------------------
#  Cette fonction affiche le PENDU
#------------------------------------------------------------

def hanged():
    printMessage("\n PENDU! ",196)
    printMessage("\n     ____________", 196);
    printMessage("     | //      |",196);
    printMessage("     |//       |",196);
    printMessage("     |/       (_)",196);
    printMessage("     |         |",196);
    printMessage("     |        /|\\",196);
    printMessage("     |         |",196);
    printMessage("     |        / \\",196);
    printMessage("    /|\\",196);
    printMessage("   / | \\",196);
    printMessage("#####################\n",196);
