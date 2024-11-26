import tkinter as tk


# Fonction pour démarrer le jeu
def demarrer_jeu(canevas,id_bouton_demarrer,id_bouton_quitter,id_bouton_options, image_alien_tk, largeur_ecran, image_vaisseau_tk):
    canevas.delete(id_bouton_demarrer)
    canevas.delete(id_bouton_quitter)
    canevas.delete(id_bouton_options)
    #mise_a_jour_score()
    global alien
    alien = canevas.create_image(200, 300, image=image_alien_tk, anchor="center")
    vaisseau = canevas.create_image(largeur_ecran/2, 600, image=image_vaisseau_tk, anchor="center")
    canevas.tag_raise(alien)
      # Démarrer le mouvement de l'Alien

# Déplacement du vaisseau
def deplacer_vaisseau(event,canevas, vaisseau, dx):
    if event.keysym == "Left":
        canevas.move(vaisseau, -dx, 0)
    elif event.keysym == "Right":
        canevas.move(vaisseau, dx, 0)

# Tirer un projectile
def tirer_projectile(event, canevas, vaisseau, projectiles):
    x, y = canevas.coords(vaisseau)
    projectile = canevas.create_oval(x - 5, y - 20, x + 5, y - 10, fill="red")
    projectiles.append(projectile)
    deplacer_projectile(projectile)

# Déplacer un projectile vers le haut
def deplacer_projectile(projectile, canevas, vitesse_projectile, projectiles, fenetre):
    if canevas.coords(projectile):
        canevas.move(projectile, 0, vitesse_projectile)
        x, y, _, _ = canevas.bbox(projectile)

        # Vérifier collision avec l'alien
        if collision(projectile, alien, canevas):
            canevas.delete(projectile)
            canevas.delete(alien)
            projectiles.remove(projectile)
            return

        # Supprimer le projectile lorsqu'il sort du canevas
        if y <= 0:
            canevas.delete(projectile)
            projectiles.remove(projectile)
        else:
            fenetre.after(20, lambda: deplacer_projectile(projectile))

# Collision entre deux objets
def collision(objet1, objet2, canevas):
    if not canevas.coords(objet1) or not canevas.coords(objet2):
        return False
    x1, y1, x2, y2 = canevas.bbox(objet1)
    xa1, ya1, xa2, ya2 = canevas.bbox(objet2)
    return not (x2 < xa1 or x1 > xa2 or y2 < ya1 or y1 > ya2)

# Fonction pour mettre à jour le score
def mise_a_jour_score(nouveau_score, canevas, id_score):
    score = nouveau_score
    canevas.itemconfig(id_score, text=f"Score: {score}")
    
# Fonction pour quitter le jeu
def quitter_jeu(fenetre):
    fenetre.quit()


# Déplacement de l'alien
def deplacer_alien(canevas, fenetre, largeur_ecran):
    canevas.move(alien, alien_dx, 0)
    x, y = canevas.coords(alien)
    if x >= largeur_ecran - 20 or x <= 20:
        alien_dx = -alien_dx
    fenetre.after(50, deplacer_alien)

def afficher_options(canevas, id_bouton_demarrer, id_bouton_quitter, id_bouton_options, largeur_ecran, bouton_option1, bouton_option2, bouton_retour):
    global id_option1, id_option2, id_retour
    # Supprimer les boutons principaux
    canevas.delete(id_bouton_demarrer)
    canevas.delete(id_bouton_quitter)
    canevas.delete(id_bouton_options)

    # Créer les boutons d'options dans le canevas
    id_option1 = canevas.create_window(largeur_ecran/2, 300, window=bouton_option1)
    id_option2 = canevas.create_window(largeur_ecran/2, 350, window=bouton_option2)
    id_retour = canevas.create_window(largeur_ecran/2, 400, window=bouton_retour)

def revenir_menu(canevas, bouton_demarrer, bouton_quitter, bouton_options, id_bouton_demarrer, id_bouton_options, id_bouton_quitter):
    # Supprimer les boutons d'options
    canevas.delete(id_option1)
    canevas.delete(id_option2)
    canevas.delete(id_retour)

    # Réafficher les boutons principaux
    id_bouton_demarrer = canevas.create_window(400, 300, window=bouton_demarrer)
    id_bouton_options = canevas.create_window(400, 350, window=bouton_options)
    id_bouton_quitter = canevas.create_window(400, 400, window=bouton_quitter)