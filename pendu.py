#!/usr/bin/python3.6
#-*-coding:utf-8
"""
    Ce programme est le TP n2 du cours Apprennez à programmer en python
    sur OpenClassRoom:
    https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-bon-vieux-pendu
    Professeur :
    Réalisé par: Ouattara Zié Aboubacar
"""
#------------------------------------------------------------
#  Import des differents modules
#------------------------------------------------------------
import donnees
from functions import *
from random import randrange, randint
import os
import pickle
#------------------------------------------------------------
# Déclaration  des variables
#------------------------------------------------------------
playAgain,errorCount,userInput,showIndice,chance = "o",0,"Aboubacar",True,8

#------------------------------------------------------------
#  Principe du jeu
#------------------------------------------------------------

#on nettoie le terminal
clearTerminal()

printMessage("\n JEU DU PENDU ", color="yellow")

principe = """
 Le principe du jeu est le suivant: L'ordinateur choisit un moi par hasard,
 vous affiche le nombre de lettres qui la compose sous forme de '-'
 et vous essayer de le deviner.
 Vous avez 8 chances et vous ne rentrer qu'une lettre à la fois.
 Si votre lettre est contenu dans le mot, l'ordinateur affiche
 la lettre à la place qu'elle occupe sinon il n'affiche rien.
 """
printMessage(principe, color="light_blue")
printMessage(" Vous pouvez aussi demander des indices en rentrant -1 en échange de 1 point de chance.", 196,214)
print("\n")

#------------------------------------------------------------
#  On vérifie si le fichier scores existes sinon il est crée
#------------------------------------------------------------
#------------------------------------------------------------
# On ouvre le fichier des scores si cela n'existe pas
# il sera crée et On demande le nom du joueur pour voir son score
#------------------------------------------------------------
name = input(" Entrer votre nom: ")
scores = None;
if not os.path.isfile("scores"):
    with open("scores", "wb") as file:
        content = {name:0}
        pickler = pickle.Pickler(file)
        pickler.dump(content)
        pass

with open("scores","rb") as file:
        scores = pickle.Unpickler(file)
        scores = scores.load()
        pass
#------------------------------------------------------------
#  Si le nom du joueur n'existe pas on le crée avec un
# score égale à 0
#------------------------------------------------------------
if name not in scores.keys():
    scores[name] = 0
#------------------------------------------------------------
#  On Affiche un Message de Bienvenu
#------------------------------------------------------------
printMessage("\n Bienvenu %s. Votre score actuel est: %d\n" %(name, scores[name]), "light_blue")


while playAgain =="O" or playAgain == "o":
    #------------------------------------------------------------
    #  On choisit un mot alétoirement contenu dans la liste des mots
    #------------------------------------------------------------
    chosenWordIndex = randint(0, len(donnees.wordsList1))
    chosenWord = donnees.wordsList1[chosenWordIndex]
    chosenWorDesc = donnees.wordsList[chosenWord]
    remainsToFind = len(chosenWord)
    wordToFindStruct = "-"*remainsToFind
    wordAlreadyFound = dict()
    #------------------------------------------------------------
    #  On refait cette action tant que le joeur n'a pas trouver
    #  le mot
    #------------------------------------------------------------
    while wordToFindStruct != chosenWord and chance > 0:
        #------------------------------------------------------------
        #  On affiche le nombre de caractères que contient
        #  le mot
        #------------------------------------------------------------

        printMessage("Le mot choisi est de cette forme: %s : %d lettre(s) reste à trouver. Tentatives restant : %d"
        %(wordToFindStruct, remainsToFind, chance), "yellow")

        #------------------------------------------------------------
        #   On demande au joueur d'entre un lettre
        #------------------------------------------------------------
        while len(userInput) > 1:
            if errorCount > 0:
                printMessage("Vous ne devez entrer qu'une seule lettre.", 196)
            userInput = input(" Entrer une lettre : ")
            try:
                userInput = int(userInput)
                if showIndice and userInput == -1:
                    printMessage("Indice: %s" %(chosenWorDesc), "light_blue")
                    showIndice = False
                    chance -=1
                elif showIndice == False:
                    printMessage("Vous avez déja utilisé l'indice!", 196)
                userInput = str("Aboubacar")
                errorCount = 0
                pass
            except ValueError as e:
                errorCount+=1
                continue
        errorCount = 0
        #------------------------------------------------------------
        #  On vérifie si la lettre est contenu dans le mot
        #------------------------------------------------------------
        if userInput in chosenWord:

            #------------------------------------------------------------
            #   On selectionne les positions correspondant à la
            #   la lettre dans le mot
            #------------------------------------------------------------
            position = [i for i,val in enumerate(chosenWord) if userInput == val]

            #------------------------------------------------------------
            #   On vérifie si la lettre a déjà été trouver au moins 1 fois
            #   Si oui on selectionne les position déja utilisé
            #   et on les enlève dans la liste des positions
            #------------------------------------------------------------
            if userInput in wordAlreadyFound.values():
                positionAlreadyUsed = [i for i,d in wordAlreadyFound.items() if d == userInput]
                position =[j for j in position if j not in positionAlreadyUsed]

            #------------------------------------------------------------
            #   On vérifie si la taille des position est superieur
            #   à 0. Si c'est le cas on ajoute la lettre trouver
            #   dans le dictionnaires contenant les lettres trouver
            #   avec leurs position dans le mot originale
            #   Sinon cela veut dire que la lettre à déjà été utilisé
            #   on affiche alors le message au joueur
            #------------------------------------------------------------
            if len(position) > 0:
                position = position[0]
                wordAlreadyFound[position] = userInput
                wordToFindInArray = list(wordToFindStruct)
                wordToFindInArray[position] = userInput
                wordToFindStruct = str().join(wordToFindInArray)
                remainsToFind -=1
                if wordToFindStruct != chosenWord:
                    printMessage("Lettre Trouvée!", 46)
                else:
                    #------------------------------------------------------------
                    #  On ajoute la chance restante dans le score du joueur
                    #------------------------------------------------------------
                    if name in scores.keys():
                        scores[name] +=chance
                    else:
                        scores[name] = chance
                    #------------------------------------------------------------
                    #  On enregistre le score dans le fichier scores
                    #------------------------------------------------------------
                    with open("scores", "wb") as file:
                        my_pickler = pickle.Pickler(file)
                        my_pickler.dump(scores)
                        pass
                    #------------------------------------------------------------
                    #  On affiche un message au joueur lui disant qui à
                    #  trouver le mot
                    #------------------------------------------------------------
                    printMessage("\n Mot trouvé! Le mot était : %s" %(wordToFindStruct),46)
            else:
                printMessage("La lettre %s est déjà utilisé" %(userInput),196)
                chance -=1 # on soustrait 1 de la chance restant
                if chance <= 0:
                    printMessage("\n Le mot rechercher était: %s" %(chosenWord), "yellow")
                    hanged()
        else:
            #------------------------------------------------------------
            #  On soustrait 1 de la chance et si il n'a reste plus
            #  le joueur a perdu
            #------------------------------------------------------------
            chance -=1
            if chance > 0:
                printMessage("Pas de chance!", 196)
            else:
                printMessage("\n Le mot rechercher était: %s" %(chosenWord), "yellow")
                hanged()
        userInput = str("Aboubacar")
    #------------------------------------------------------------
    #  Fin du jeu on demande au joueur s'il veut rejouer!
    #------------------------------------------------------------
    playAgain = "I don't know"
    while playAgain !="n" and playAgain !="N" and playAgain !="O" and playAgain != "o":
        if errorCount > 0:
            printMessage("Les choix que vous avez sont: o, O, n ou N!", "yellow")
        playAgain = input(" Voulez-vous réjouer? o ou O => Oui et n ou N => non :")
        errorCount += 1
    if playAgain !="O" and playAgain != "o":
        printMessage("\n Votre score est : %d " %(scores[name]), "46")
        printMessage("\n FIN DU JEU! MERCI D'AVOIR JOUER \n", "light_blue")
    else:
        errorCount = 0
        showIndice = True
        chance = 8
        userInput = str("Aboubacar")
        clearTerminal()
