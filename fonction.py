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

# Fonction pour déplacer l'Alien
def deplacer_alien():
    # Déplacer l'Alien
    pg.canevas.move(pg.alien, pg.dx, 0)

    # Obtenir les coordonnées de l'Alien
    x1, y1, x2, y2 = pg.canevas.coords(pg.alien)

    # Vérifier les collisions avec les bords du canevas
    if x2 >= pg.canvas_width or x1 <= 0:
        pg.dx = -pg.dx  # Inverser la direction

    # Relancer la  fonction après un délai pour animer le mouvement
    pg.fenetre.after(20, deplacer_alien)

def afficher_options():
    # Masquer le bouton de base
    pg.bouton_options.pack_forget()
    
    # Afficher les nouveaux boutons
    pg.bouton_option1.pack(pady=5)
    pg.bouton_option2.pack(pady=5)
    pg.bouton_retour.pack(pady=5)

def revenir_arriere():
    # Masquer les nouveaux boutons
    pg.bouton_option1.pack_forget()
    pg.bouton_option2.pack_forget()
    pg.bouton_retour.pack_forget()
    
    # Réafficher le bouton de base
    pg.bouton_options.pack(pady=20)
