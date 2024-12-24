# Faire une boucle infinie qui s'arrête si on saisit le nombre "0"
# compter le nombre de fois dont on a saisit un nombre compris entre 0 et 100 : compteur_0_100
# compter le nombre de fois dont on a saisit un nombre compris entre 101 et 1000 : compteur_101_1000
# compter le nombre de fois dont on a saisit un nombre supérieur à 1000 : compteur_1001

compteur_0_100=0
compteur_101_1000=0
compteur_1001=0
while(True):
    nombre=int(input("Nombre:"))
    if nombre==0:
        break
    if 0<nombre<=100:
        compteur_0_100+=1
    elif 100<nombre<=1000:
        compteur_101_1000+=1
    elif 1000<nombre:
        compteur_1001+=1

print("[0,100] : ", compteur_0_100)
print("[101,1000] : ", compteur_101_1000)
print("[1001,infini] : ", compteur_1001)