import fonction as fct
import tkinter as tk


# Vitesse initiale de l'Alien
dx = 5

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu Tkinter")
fenetre.geometry("600x500")

# Création du menu
menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)



# Nouveaux boutons (créés mais non affichés au départ)


# Création du canevas pour la zone de jeu
canvas_width = 400
canvas_height = 300

canevas = tk.Canvas(fenetre, width=canvas_width, height=canvas_height, bg="black")
canevas.pack(pady=20)

# Affichage du score
score = 0
label_score = tk.Label(fenetre, text="Score: 0", font=("Arial", 14), fg="white", bg="black")

# Création des boutons sur le canevas
bouton_demarrer = tk.Button(fenetre, text="Démarrer le jeu", command=fct.demarrer_jeu, fg="black", highlightbackground="black")

bouton_options = tk.Button(fenetre, text='Options', command=fct.afficher_options, fg="black", highlightbackground="black")

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fct.quitter_jeu, fg="black", highlightbackground="black")

bouton_option1 = tk.Button(fenetre, text="Option 1", font=("Arial", 14), fg="white", bg="black")
bouton_option2 = tk.Button(fenetre, text="Option 2", font=("Arial", 14), fg="white", bg="black")
bouton_retour = tk.Button(fenetre, text="Retour", font=("Arial", 14), fg="white", bg="black", command=fct.revenir_arriere)

# Placement des boutons sur le canevas avec create_window
canevas.create_window(canvas_width // 2, 20, window=label_score, anchor="n")
canevas.create_window(100, 250, window=bouton_demarrer)  # Positionne le bouton "Démarrer le jeu"
canevas.create_window(300, 250, window=bouton_quitter)   # Positionne le bouton 
canevas.create_window(200, 100, window=bouton_options)


# Création de l'Alien (ici un rectangle)
#alien = canevas.create_rectangle(50, 100, 100, 150, fill="green")


# Lancer le mouvement de l'Alien
#fct.deplacer_alien()

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()