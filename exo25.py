liste=[]
while(True):
    nombre=int(input("Nombre:"))
    liste.append(nombre)
    if len(liste)>=3 and liste[-1]>liste[-2] and liste[-2]>liste[-3]:
        break