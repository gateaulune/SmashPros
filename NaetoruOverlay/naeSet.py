import tkinter as tk

def create_text_with_outline(canvas, x, y, text, font, main_color, outline_color, outline_width=2):
    # Dessiner le texte principal
    canvas.create_text(x, y, text=text, font=font, fill=main_color)

    # Dessiner le texte avec un décalage vers le haut pour l'effet de contour
    canvas.create_text(x, y - outline_width, text=text, font=font, fill=outline_color)

    # Dessiner le texte avec un décalage vers le bas
    canvas.create_text(x, y + outline_width, text=text, font=font, fill=outline_color)

    # Dessiner le texte avec un décalage vers la gauche
    canvas.create_text(x - outline_width, y, text=text, font=font, fill=outline_color)

    # Dessiner le texte avec un décalage vers la droite
    canvas.create_text(x + outline_width, y, text=text, font=font, fill=outline_color)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Texte avec contour")

# Créer le canevas
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Définir la police et les couleurs
custom_font = ("Arial", 16)
text_color = "blue"
outline_color = "red"

# Utiliser la fonction pour créer le texte avec contour
create_text_with_outline(canvas, 150, 100, "Hello, Outline!", custom_font, text_color, outline_color)

# Lancer la boucle principale
root.mainloop()
