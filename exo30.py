#   public-ip est une librairie téléchargée grâce à PIP depuis 
#   https://pypi.org/project/public-ip/
#   Installation : pip install public-ip
#   Méthode "get" : retourne l'adresse IP publique du réseau auquel on est connecté

import public_ip as ip

print("Adresse publique:" + ip.get())