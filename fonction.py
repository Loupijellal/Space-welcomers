import tkinter as tk


# Fonction pour démarrer le jeu
def demarrer_jeu(canevas):
    canevas.delete(pg.id_bouton_demarrer)
    canevas.delete(pg.id_bouton_quitter)
    canevas.delete(pg.id_bouton_options)
    global score
    global alien
    #mise_a_jour_score()
    alien = canevas.create_image(200, 300, image=pg.image_alien_tk, anchor="center")
    print("ajout alien")
    canevas.tag_raise(alien)
      # Démarrer le mouvement de l'Alien

# Déplacement du vaisseau
def deplacer_vaisseau(event):
    if event.keysym == "Left":
        pg.canevas.move(vaisseau, -dx, 0)
    elif event.keysym == "Right":
        pg.canevas.move(vaisseau, dx, 0)

# Tirer un projectile
def tirer_projectile(event):
    x, y = pg.canevas.coords(vaisseau)
    projectile = pg.canevas.create_oval(x - 5, y - 20, x + 5, y - 10, fill="red")
    pg.projectiles.append(projectile)
    deplacer_projectile(projectile)

# Déplacer un projectile vers le haut
def deplacer_projectile(projectile):
    if pg.canevas.coords(projectile):
        pg.canevas.move(projectile, 0, vitesse_projectile)
        x, y, _, _ = pg.canevas.bbox(projectile)

        # Vérifier collision avec l'alien
        if collision(projectile, alien):
            pg.canevas.delete(projectile)
            pg.canevas.delete(alien)
            pg.projectiles.remove(projectile)
            return

        # Supprimer le projectile lorsqu'il sort du canevas
        if y <= 0:
            pg.canevas.delete(projectile)
            pg.projectiles.remove(projectile)
        else:
            pg.fenetre.after(20, lambda: deplacer_projectile(projectile))

# Collision entre deux objets
def collision(objet1, objet2):
    if not pg.canevas.coords(objet1) or not pg.canevas.coords(objet2):
        return False
    x1, y1, x2, y2 = pg.canevas.bbox(objet1)
    xa1, ya1, xa2, ya2 = pg.canevas.bbox(objet2)
    return not (x2 < xa1 or x1 > xa2 or y2 < ya1 or y1 > ya2)

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


# Déplacement de l'alien
def deplacer_alien():
    pg.canevas.move(alien, pg.alien_dx, 0)
    x, y = pg.canevas.coords(alien)
    if x >= pg.canvas_width - 20 or x <= 20:
        pg.alien_dx = -pg.alien_dx
    pg.fenetre.after(50, deplacer_alien)

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