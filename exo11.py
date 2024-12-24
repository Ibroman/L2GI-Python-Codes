from random import randint

inconnu=randint(0,10)
#inconnu=8
essai=5

for i in range(essai):
    nombre=int(input("Nombre:"))
    if nombre==inconnu:
        print("Bravo !")
        break
    else:
        print("Réessayez")
    
    if i==(essai-1):
        print("Echec !", inconnu)

