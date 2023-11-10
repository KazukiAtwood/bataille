# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:28:09 2023

@author: 33760
"""

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.tab = []

    def ajouter_carte(self, carte):
        self.tab.append(carte)

    def retirer_carte(self):
        return self.tab.pop(0)

    def nb_reste(self):
        return len(self.tab)