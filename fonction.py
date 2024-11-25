import tkinter as tk
import programme as pg


# Fonction pour démarrer le jeu
def demarrer_jeu():
    pg.canevas.delete(pg.id_bouton_demarrer)
    pg.canevas.delete(pg.id_bouton_quitter)
    pg.canevas.delete(pg.id_bouton_options)
    global score
    global alien
    mise_a_jour_score()
    alien = pg.canevas.create_image(200, 300, image=pg.image_alien_tk, anchor="center")
    pg.canevas.tag_raise(alien)
      # Démarrer le mouvement de l'Alien

# Fonction pour mettre à jour le score
def mise_a_jour_score(nouveau_score):
    global score
    score = nouveau_score
    pg.canevas.itemconfig(pg.id_score, text=f"Score: {score}")
    
# Fonction pour quitter le jeu
def quitter_jeu():
    pg.fenetre.quit()

# initialisation de la classe monstre
class Monstres:
    def __init__(monstre):
        monstre.position = (0,0)
        monstre.couleur = str
        monstre.vie = 0


# Fonction pour déplacer l'Alien
def deplacer_alien(alien):
    # Déplacer l'Alien
    pg.canevas.move(alien, pg.dx, 0)

    # Obtenir les coordonnées de l'Alien
    x1, y1, x2, y2 = pg.canevas.coords(alien)

    # Vérifier les collisions avec les bords du canevas
    if x2 >= pg.canvas_width or x1 <= 0:
        pg.dx = -pg.dx  # Inverser la direction

    # Relancer la  fonction après un délai pour animer le mouvement
    pg.fenetre.after(20, lambda: deplacer_alien(alien))

def afficher_options():
    global id_option1, id_option2, id_retour
    
    # Supprimer les boutons principaux
    pg.canevas.delete(pg.id_bouton_demarrer)
    pg.canevas.delete(pg.id_bouton_quitter)
    pg.canevas.delete(pg.id_bouton_options)

    # Créer les boutons d'options dans le canevas
    id_option1 = pg.canevas.create_window(pg.largeur_ecran/2, 300, window=pg.bouton_option1)
    id_option2 = pg.canevas.create_window(pg.largeur_ecran/2, 350, window=pg.bouton_option2)
    id_retour = pg.canevas.create_window(pg.largeur_ecran/2, 400, window=pg.bouton_retour)

def revenir_menu():
    global id_option1, id_option2, id_retour

    # Supprimer les boutons d'options
    pg.canevas.delete(id_option1)
    pg.canevas.delete(id_option2)
    pg.canevas.delete(id_retour)

    # Réafficher les boutons principaux
    pg.id_bouton_demarrer = pg.canevas.create_window(400, 300, window=pg.bouton_demarrer)
    pg.id_bouton_options = pg.canevas.create_window(400, 350, window=pg.bouton_options)
    pg.id_bouton_quitter = pg.canevas.create_window(400, 400, window=pg.bouton_quitter)