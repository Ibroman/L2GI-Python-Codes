# Application : Calculer la remise et afficher la montant à payer
# - remise = 0 SI montant<5000
# - remise = 10% de montant SI 5000<=montant<10000
# - remise = 0% de montant SI 10000<montant
# - le montant a payer on lui applique une TVA de 15%

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
