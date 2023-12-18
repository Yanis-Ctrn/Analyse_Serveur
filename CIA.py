import pandas as pd
import json

if __name__ == "__main__":
    pass

nomServ = pd.read_csv("serveurs.csv",encoding='latin-1').drop_duplicates() #récupère les serveurs que l'on souhaite testé en supprimant les doublons s'il y en a 
resultat = "resultat.txt" #fichier resultat

appli_perimetre = [] #tableau contenant les applications du périmètre 

# Fonction permettant de récupérer les applications ayant comme code CIA celui recherché
def Appli(data_p, CIA):
    for application in data_p:
        if application["cia"] == CIA:
            appli_perimetre.append(application["cia"])

# Fonction permettant de comparé les variables entre elles 
def Verif(data_s, present):
    for serveur in data_s:   
        nom = serveur["serveur"]
        cia = serveur["cia"]
        cia_bt = serveur["cia_bt"]
        for ligne in nomServ['serveur']:    #serveur test 
            serveur_trouve = False 
            if nom == ligne:
                if cia_bt == None :
                    if cia == None:
                        serveur_trouve = True
                        break
                    else :
                        for cia_p in appli_perimetre: # les cia de notre permitre      
                            if cia == cia_p:
                                present.append(f"{ligne} -- Appli :  " + cia)
                                serveur_trouve = True
                                break
                else : 
                    for cia_p in appli_perimetre: # les cia de notre permitre      
                            if cia_bt == cia_p:
                                present.append(f"{ligne} -- Appli :  " + cia_bt)
                                serveur_trouve = True
                                break                            
                if serveur_trouve == False:
                    pass
        
def Write(present , CIA):
    with open(resultat, 'w') as fichier:
        fichier.write("     Voici la liste des serveur ayant comme code CIA : " + CIA + "\n \n \n")
        for serveur in present:
            fichier.write(serveur + "\n")

def LaunchC(CIA):
    with open ("info_api_p.json", 'r') as api_p:
        data_p = json.load(api_p)

    with open ("info_api_s.json", 'r') as api_s:
        data_s = json.load(api_s)
    present = [] # tableau contenant les serveur présent dans notre périmètre
    Appli(data_p, CIA)
    Verif(data_s, present)
    Write(present , CIA)
