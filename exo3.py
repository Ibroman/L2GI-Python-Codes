# Application : Afficher la table de multiplication d'un nombre
# - 1) Avec une boucle "while"
# - 2) Avec une boucle "for"

nombre=int(input("Nombre:"))
i=1
while(i<=10):
    print(nombre, "X", i, "=", nombre*i)
    i+=1

for i in range(1,11):
    print(nombre, "X", i, "=", nombre*i)