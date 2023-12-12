import json
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

def Delete():
    # Suppression des anciennes données de l'api 
    with open("info_api_p.json", 'w') as fichier:
        json.dump({}, fichier) 

    with open("info_api_s.json", 'w') as fichier:
        json.dump({}, fichier)

def Update():
    # Mise a jour des données issus de l'api
    with open("info_api_p.json", 'w') as fichier:
        json.dump(list_perim.json, fichier) 

    with open("info_api_s.json", 'w') as fichier:
        json.dump(list_serv.json, fichier)


