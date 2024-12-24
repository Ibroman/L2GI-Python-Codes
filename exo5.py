nombre=int(input("Donner un nombre:"))
notes=[]
somme=0
for i in range(nombre):
    n=int(input("nombre:"))
    if n>=0 and n<=100:
        notes.append(n)
        somme+=n
moyenne=somme/nombre
moyenne2=sum(notes)/len(notes)
print("Moyenne=",moyenne)
print("Moyenne2=",moyenne2)
print(notes)
