nombres=[]
compteur=0
for i in range(10):
    n = int(input("Donner un nombre:"))
    nombres.append(n)
    if n > 1000:
        compteur+=1
print(f"Nombre > 1000 est égale à {compteur}")