# Créer un Jeu :
# - générer un nombre entier aléatoire X
# - l'utilisateur saisit un nombre pour déviner X
# - nombre == X ==> afficher "Bravo !!!"
# - Distance entre X et nombre < 5 ==> afficher "Très proche..."
# - Distance entre X et nombre < 10 ==> afficher "Proche..."
# - Distance entre X et nombre < 20 ==> afficher "Très loin..."

import random
x=random.randint(1,50)
compteur=0
while(True):
    nombre=int(input("Nombre:"))
    if nombre==x:
        print("Bravo !!!")
        break
    compteur+=1
    if compteur==5:
        print("Echec !!!")
        break
    pas=abs(x-nombre)
    if pas<10:
        print("Très proche...")
    elif pas<20:
        print("Proche...")
    else:
        print("Très loin...")