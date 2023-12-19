import pandas as pd
import json 

if __name__ == "__main__":
    pass

nomServ = pd.read_csv("serveurs.csv",encoding='latin-1').drop_duplicates() #récupère les serveurs que l'on souhaite testé en supprimant les doublons s'il y en a 

appli_perimetre = [] #tableau contenant les applications du périmètre 

# Fonction permettant de récupérer les serveurs issus du périmètre donnée 
def Appli(data_p, perimetre):
    for application in data_p:
        if application["name_department"] == perimetre:
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
                                print("1")
                                break                            
                if serveur_trouve == False:
                    pass

def Write(present):
    # Séparer les noms des serveurs et des applications
    data = [entry.split(' -- Appli :  ') for entry in present]
    
    # Créer un DataFrame à partir des données séparées
    df = pd.DataFrame(data, columns=['Serveur', 'Application'])
    
    # Écrire le DataFrame dans un fichier CSV
    df.to_csv('resultat.csv', index=False)

def LaunchP(perimetre):
    with open ("data/info_api_p.json", 'r') as api_p:
        data_p = json.load(api_p)

    with open ("data/info_api_s.json", 'r') as api_s:
        data_s = json.load(api_s)
    present = [] # tableau contenant les serveur présent dans notre périmètre
    Appli(data_p ,perimetre)
    Verif(data_s, present)
    Write(present)


