import tkinter as tk
import programme as pg
from tkinter import messagebox

# Fonction pour démarrer le jeu
def demarrer_jeu():
    global score
    score = 0
    mise_a_jour_score()

# Fonction pour mettre à jour le score
def mise_a_jour_score():
    pg.label_score.config(text=f"Score: {score}")

# Fonction pour quitter le jeu
def quitter_jeu():
    pg.fenetre.quit()

# Fonction pour afficher une option dans le menu
def afficher_option():
    messagebox.showinfo("Option", "Option sélectionnée")

# initialisation de la classe monstre
class Monstres:
    def __init__(monstre):
        monstre.position = (0,0)
        monstre.couleur = str
        monstre.vie = 0

monstres = [Monstres() for _ in range(3)]
