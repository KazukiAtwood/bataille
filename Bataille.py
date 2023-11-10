import random
from Carte import * 
from Joueur import *

class Bataille:
    def __init__(self):
        self.cartes = []
        self.joueurs = [Joueur("Patrick"), Joueur("Titouan")]
        self.cartes_spe = {"As": 14, "Roi": 13, "Dame": 12, "Valet": 11}
        self.tours = 0
        self.victoires_j1 = 0
        self.victoires_j2 = 0
        self.max_tours = 10

    def commencer(self):
        familles = ["Coeur", "Carreau", "Trèfle", "Pique"]
        for famille in familles:
            for valeur in range(2, 15):
                carte = Carte(valeur, famille)
                self.cartes.append(carte)

    def distribution(self):
        random.shuffle(self.cartes)
        while self.cartes:
            for joueur in self.joueurs:
                joueur.ajouter_carte(self.cartes.pop())

    def bataille(self):
        while self.tours < self.max_tours:
            self.tours += 1
            print(f"Tour {self.tours}:")

            if any(joueur.nb_reste() == 0 for joueur in self.joueurs):
                print("\n ----- Plus de cartes, fin de la partie ! -----\n")
                break

            carte_j1 = self.joueurs[0].retirer_carte()
            carte_j2 = self.joueurs[1].retirer_carte()

            print(f"{self.joueurs[0].nom} pose la carte : {carte_j1}")
            print(f"{self.joueurs[1].nom} pose la carte : {carte_j2}")

            if self.comparer_cartes(carte_j1, carte_j2):
                print("Le Joueur 1 gagne ce tour.\n")
                print("-------------------------- \n")
                self.joueurs[0].ajouter_carte(carte_j1)
                self.joueurs[0].ajouter_carte(carte_j2)
                self.victoires_j1 += 1
            else:
                print("Le Joueur 2 gagne ce tour.\n")
                print("-------------------------- \n")
                self.joueurs[1].ajouter_carte(carte_j1)
                self.joueurs[1].ajouter_carte(carte_j2)
                self.victoires_j2 += 1

    def comparer_cartes(self, carte1, carte2):
        val1 = carte1.valeur if not isinstance(carte1.valeur, str) else self.cartes_spe[carte1.valeur]
        val2 = carte2.valeur if not isinstance(carte2.valeur, str) else self.cartes_spe[carte2.valeur]

        if val1 == val2:
            self.supprimer_egalite(val1)
            print("C'est une égalité ! La bataille continue !\n")
            return False
        else:
            return val1 > val2

    def supprimer_egalite(self, valeur):
        for joueur in self.joueurs:
            joueur.tab = [carte for carte in joueur.tab if (isinstance(carte.valeur, str) or carte.valeur != valeur)]

    def nb_reste(self):
        for joueur in self.joueurs:
            print(f"Carte(s) restante pour {joueur.nom}: {joueur.nb_reste()}")
            
    def vainqueur(self):
        if (self.victoires_j1 > self.victoires_j2):
            print(f"{self.joueurs[0].nom} a gagné !")
        elif (self.victoires_j2 > self.victoires_j1):
            print(f"{self.joueurs[1].nom} a gagné !")
        else: 
            print("Egalité pour les 2 joueurs")

    def lancement(self):
        self.commencer()
        self.distribution()
        self.bataille()
        self.vainqueur()
        print(f"Nombre de victoires pour {self.joueurs[0].nom}: {self.victoires_j1}")
        print(f"Nombre de victoires pour {self.joueurs[1].nom}: {self.victoires_j2}")
        self.nb_reste()

jeu_bataille = Bataille()
jeu_bataille.lancement()