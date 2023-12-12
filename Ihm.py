from tkinter import *
from Perimetre import LaunchP
from Cia import LaunchC
from Api import Update 

background = "white"

# Création fenetre
window = Tk()

# Personalisation de la fenètre
window.title("Analyse Serveurs")
window.geometry("1000x720")
window.resizable(width=False,height=False)
window.config(background=background)

#Configuration du titre de la page 
title = Label(window, text="Analyse Serveur",pady=20, font=("Courrier", 40), bg=background, fg="black" )
title.pack()

# Configuration du texte périmètre
perimetre_title = Label(window, text="Indiqué le périmètre : ",pady=5, font=("Courrier", 20), bg=background, fg="black" )
perimetre_title.pack()

#Configuration du champs de saisie du périmètre de l'utilisateur
perimetre_input = Entry() #prd-pep-gmi
perimetre_input.pack()

#Configuration de la fonction on_clickP pour le cliquer sur l'analyse depuis un périmètre
def on_clickP():
    user_input = perimetre_input.get()
    if user_input == "" : 
        Present_label.configure(text="Vous devez d'abord renseigné le périmètre", fg="red")
    else :
        LaunchP(user_input)
        Present_label.configure(text = "Le résultat a bien été chargé dans le fichier texte", fg="black")

# Configuration du bouton pour rechercher selon un Perimètre donnée
boutonPerimetre = Button(window, text="Recherche par périmètre", command=on_clickP)
boutonPerimetre.pack(pady=20)

# Configuration du texte périmètre
Cia_title = Label(window, text="Indiqué directement le code CIA : ",pady=5, font=("Courrier", 20), bg=background, fg="black" )
Cia_title.pack()

#Configuration du champs de saisie du périmètre de l'utilisateur
Cia_input = Entry() #prd-pep-gmi
Cia_input.pack()

#Configuration de la fonction on_clickC pour le clique sur l'analyse depuis un code CIA
def on_clickC():
    user_input = Cia_input.get()
    if user_input == "" :   
        Present_label.configure(text="Vous devez d'abord renseigné le code CIA", fg="red")
    else :
        LaunchC(user_input)
        Present_label.configure(text = "Le résultat a bien été chargé dans le fichier texte", fg="black")

# Configuration du bouton pour rechercher selon un Perimètre donnée
boutonCia = Button(window, text="Recherche par CIA", command=on_clickC)
boutonCia.pack(pady=20)

#Configuration du label ou apparaitera les résultats 
Present_label = Label(window, text="Ici vous retrouverez les résultats des serveurs présent pour votre périmètre",pady=75, font=("Courrier", 12), bg=background, fg="black")
Present_label.pack()


# Configuration du bouton pour quitter l'application
quitButton = Button(window, text = "Quitter", padx= 10 , pady= 20 , command = window.destroy)
quitButton.pack()

# Configuration du bouton pour mettre a jour les informations de l'api 
UpdateButton = Button(window, text="Mettre a jour les données de l'api", command = Update())
UpdateButton.pack()

# Configuration du label contenant les informations de la dernière mise a jour de l'api 
Update_label = Label(window, text="")


# Afficher 
window.mainloop()