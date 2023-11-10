# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:28:33 2023

@author: 33760
"""

class Carte:
    def __init__(self, valeur, famille):
        self.valeur = valeur
        self.famille = famille

    def __str__(self):
        return f"{self.valeur} de {self.famille}"
    
    