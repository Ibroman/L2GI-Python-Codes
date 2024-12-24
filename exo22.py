liste=(-5,-20,0,10,20,30)
positif=[]
negatif=[]
for i in liste:
    if i>=0:
        positif.append(i)
    else:
        negatif.append(i)

print("Positif:", positif)
print("Négatif:", negatif)