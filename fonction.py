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

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu Tkinter")
fenetre.geometry("600x500")

# Création du menu
menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)

# Ajout d'un menu déroulant avec quelques options
menu_options = tk.Menu(menu_bar, tearoff=0)
menu_options.add_command(label="Option 1", command=afficher_option)
menu_options.add_command(label="Option 2", command=afficher_option)
menu_options.add_separator()
menu_options.add_command(label="Quitter", command=quitter_jeu)
menu_bar.add_cascade(label="Options", menu=menu_options)

# Création du canevas pour la zone de jeu
canevas = tk.Canvas(fenetre, width=400, height=300, bg="black")
canevas.pack(pady=20)

# Affichage du score
score = 0
label_score = tk.Label(fenetre, text="Score: 0", font=("Arial", 14))
label_score.pack()

# Création des boutons sur le canevas
bouton_demarrer = tk.Button(fenetre, text="Démarrer le jeu", command=demarrer_jeu)
bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter_jeu)

# Placement des boutons sur le canevas avec create_window
canevas.create_window(100,100, window=label_score)
canevas.create_window(100, 250, window=bouton_demarrer)  # Positionne le bouton "Démarrer le jeu"
canevas.create_window(300, 250, window=bouton_quitter)   # Positionne le bouton 

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()

#n'importe quoi bbzdqddfgd