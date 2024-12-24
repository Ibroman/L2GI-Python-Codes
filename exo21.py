nombre = 20
compteur = 0
while(True):
    compteur +=1
    essai = int(input("Donner un nombre:"))
    if essai == nombre:
        break

print("Essai:", compteur)