import fonction as fct
import tkinter as tk
from PIL import Image, ImageTk 

# Variables globales pour le déplacement et le tir
dx = 5  # Vitesse horizontale du vaisseau
vitesse_projectile = -10
projectiles = []  # Liste des projectiles actifs
alien_dx = 5  # Vitesse horizontale de l'alien

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight() - 200
fenetre.title("Jeu Tkinter")
fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}")  # Taille de la fenêtre

# Charger l'image de fond
image_fond = Image.open("/Users/gaspardc/Documents/CPE Lyon/Csdev/Space-welcomers/jikko2.jpeg")  # Chemin de l'image
image_fond = image_fond.resize((largeur_ecran, hauteur_ecran), Image.Resampling.LANCZOS)  # Redimensionner l'image
image_fond_tk = ImageTk.PhotoImage(image_fond)

# Charger les images du vaisseau et de l'alien
image_vaisseau = Image.open("/Users/gaspardc/Documents/CPE Lyon/Csdev/Space-welcomers/jinx.png")
image_vaisseau = image_vaisseau.resize((60, 40), Image.Resampling.LANCZOS)
image_vaisseau_tk = ImageTk.PhotoImage(image_vaisseau)

# Charger l'image de l'Alien
image_alien = Image.open("/Users/gaspardc/Documents/CPE Lyon/Csdev/Space-welcomers/ekko.png")  # Remplacez par le chemin de votre image
image_alien = image_alien.resize((40, 40), Image.Resampling.LANCZOS)  # Redimensionner si nécessaire
image_alien_tk = ImageTk.PhotoImage(image_alien)

# Création du canevas
canvas_width = image_fond_tk.width()
canvas_height = image_fond_tk.height()
canevas = tk.Canvas(fenetre, width=canvas_width, height=canvas_height)
canevas.pack(fill="both", expand=True)

# Affichage de l'image de fond
#image_fond_id = canevas.create_image(0, 0, anchor="nw", image=image_fond_tk, tags="fond")
print("ajout fond")

# Affichage du score sur le canevas
score = 0
id_score = canevas.create_text(
    largeur_ecran/2, 30,  # Position du texte (au milieu en haut)
    text=f"Score: {score}",
    font=("Arial", 20, "bold"),
    fill="white"
)

bouton_option1 = tk.Button(fenetre, text="Option 1", font=("Arial", 14), fg="white", bg="black", highlightbackground="black", highlightthickness=0)
bouton_option2 = tk.Button(fenetre, text="Option 2", font=("Arial", 14), fg="white", bg="black", highlightbackground="black", highlightthickness=0)
bouton_retour = tk.Button(fenetre, text="Retour", command=fct.revenir_menu, font=("Arial", 14), fg="white", bg="black", highlightbackground="black", highlightthickness=0)

# Création des boutons sur le canevas
bouton_demarrer = tk.Button(fenetre, text="Démarrer le jeu", command=lambda: fct.demarrer_jeu(canevas), fg="black", highlightbackground="black")
bouton_options = tk.Button(fenetre, text="Options", command=fct.afficher_options, fg="black", highlightbackground="black")
bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit, fg="black", highlightbackground="black")

# Placement des boutons sur le canevas
id_bouton_demarrer = canevas.create_window(largeur_ecran/2, 300, window=bouton_demarrer)
id_bouton_options = canevas.create_window(largeur_ecran/2, 350, window=bouton_options)
id_bouton_quitter = canevas.create_window(largeur_ecran/2, 400, window=bouton_quitter)

# Lier les touches clavier
fenetre.bind("<Left>", fct.deplacer_vaisseau)
fenetre.bind("<Right>", fct.deplacer_vaisseau)
fenetre.bind("<space>", fct.tirer_projectile)

# création du vaisseau 
#vaisseau = canevas.create_oval()
# Lancer le mouvement de l'Alien
#fct.deplacer_alien()

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()