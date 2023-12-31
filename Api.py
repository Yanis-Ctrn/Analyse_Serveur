import requests
from requests.auth import HTTPDigestAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == "__main__":
    pass

def extract_json_objects(text):
    # Utilise une expression régulière pour trouver des objets JSON entre {},
    # en ignorant les {} entre guillemets
    pattern = r'\{(?:[^{}"]|"(?:\\.|[^"\\])*")*\}'
    return re.findall(pattern, text)

def stream_to_file(url, file_name, auth):
    with requests.get(url, auth=auth, stream=True, verify=False) as r:
        r.raise_for_status()

        with open(file_name, 'w') as file:
            file.write("[")
            current_chunk = ''
            first_objet = True
            
            for chunk in r.iter_content(chunk_size=8192, decode_unicode=True):
                current_chunk += chunk
                # Recherchez des objets JSON complets dans le chunk
                objects = extract_json_objects(current_chunk)
                for obj in objects:
                    if first_objet == True:
                        file.write(obj + "\n")
                        first_objet = False
                    # Copiez chaque objet JSON en entier dans le fichier
                    else :
                        file.write("," + obj + "\n")
                # Réinitialisez le chunk pour le prochain tour de boucle
                current_chunk = ''
            file.write("]") 

def Update():
    username = 'catarinoya'
    password = 'QBVMaq237!.bmzW.yctv'
    url_perimetre = "https://cockpit.intranatixis.com/query/api/json/174"
    url_serveur = "https://cockpit.intranatixis.com/query/api/json/260"
    
    print("0")
    stream_to_file(url_perimetre, "info_api_p.json", (username, password))
    print("1")
    stream_to_file(url_serveur, "info_api_s.json", (username, password))
    print("2")
