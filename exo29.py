#   camelcase est une librairie téléchargée grâce à PIP depuis 
#   https://pypi.org/project/camelcase/
#   Installation : pip install camelcase
#   Méthode "hump" : retourne la chaîne passée en paramètre en camelcase

import camelcase

c = camelcase.CamelCase()
nom = input("Donner votre nom:")
print(c.hump(nom))