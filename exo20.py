liste=(-5,-20,0,10,20,30)
positif=0
negatif=0
for i in liste:
    if i>=0:
        positif +=i
    else:
        negatif +=i

print("Positif:", positif)
print("Négatif:", negatif)