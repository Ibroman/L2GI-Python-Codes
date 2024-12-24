designation=input("Désignation:")
prix=float(input("Prix:"))
quantite=int(input("Quantité:"))
montant=prix*quantite
if montant<5000:
    remise=0
elif montant<10000:
    remise=montant*0.1
else:
    remise=montant*0.2
print("Montant=", (montant-remise)*1.15)
