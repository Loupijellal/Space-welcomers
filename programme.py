import fonction as fct
import tkinter as tk


# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu Tkinter")
fenetre.geometry("600x500")

# Création du menu
menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)

# Ajout d'un menu déroulant avec quelques options
menu_options = tk.Menu(menu_bar, tearoff=0)
menu_options.add_command(label="Option 1", command=fct.afficher_option)
menu_options.add_command(label="Option 2", command=fct.afficher_option)
menu_options.add_separator()
menu_options.add_command(label="Quitter", command=fct.quitter_jeu)
menu_bar.add_cascade(label="Options", menu=menu_options)

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

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fct.quitter_jeu, fg="black", highlightbackground="black")

# Placement des boutons sur le canevas avec create_window
canevas.create_window(canvas_width // 2, 20, window=label_score, anchor="n")
canevas.create_window(100, 250, window=bouton_demarrer)  # Positionne le bouton "Démarrer le jeu"
canevas.create_window(300, 250, window=bouton_quitter)   # Positionne le bouton 

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()