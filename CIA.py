import pandas as pd
import requests
from requests.auth import HTTPDigestAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == "__main__":
    pass

username = 'catarinoya'
password = 'QBVMaq237!.bmzW.yctv'

url_serveur = "https://cockpit.intranatixis.com/query/api/json/260" #Url de l'api permettant la récupération des périmètre et leur application 
url_perimetre = "https://cockpit.intranatixis.com/query/api/json/174" #Url de l'api permettant la récupération des périmètre et leur application 

list_perim = requests.get(url_perimetre, auth=(username, password), verify=False) #récupètre la liste des périmètres ainsi que les applications qu'ils gèrent
list_serv = requests.get(url_serveur, auth=(username, password), verify=False) #récupètre la liste des serveurs connu avec leurs code IUA
nomServ = pd.read_csv("serveurs.csv",encoding='latin-1').drop_duplicates() #récupère les serveurs que l'on souhaite testé en supprimant les doublons s'il y en a 
resultat = "resultat.txt" #fichier resultat

donnee_s = list_serv.json() #Contenu de l'API serveur
donnee_p = list_perim.json() #Contenu de l'API perimetre

appli_perimetre = [] #tableau contenant les applications du périmètre 
present = [] # tableau contenant les serveur présent dans notre périmètre

# Fonction permettant de récupérer les applications ayant comme code CIA celui recherché
def Appli(CIA):
    for application in donnee_p:
        if application["cia"] == CIA:
            appli_perimetre.append(application["cia"])

# Fonction permettant de comparé les variables entre elles 
def Verif():
    for serveur in donnee_s:   
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
                                present.append(f"{ligne}")
                                serveur_trouve = True
                                break
                        
                else : 
                    for cia_p in appli_perimetre: # les cia de notre permitre      
                            if cia_bt == cia_p:
                                present.append(f"{ligne}")
                                serveur_trouve = True
                                break                            

                if serveur_trouve == False:
                    pass
        


def Write(CIA):
    with open(resultat, 'w') as fichier:
        fichier.write("     Voici la liste des serveur ayant comme code CIA : " + CIA + "\n \n \n")
        for serveur in present:
            fichier.write(serveur + "\n")

def LaunchC(CIA):
    Appli(CIA)
    Verif()
    Write(CIA)
