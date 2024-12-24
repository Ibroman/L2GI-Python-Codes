# Gestion des erreurs:  éviter que le programme s'arrête à cause d'une erreur
# try : déclare un bloc dont les instructions sont surveillés
# except NameError : attrape les erreurs de type NameError
# except : attrapage toutes les erreurs restantes

try:
    x = 5 + "L"
    print("Bonjour")
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")