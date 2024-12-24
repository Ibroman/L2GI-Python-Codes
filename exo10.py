principale=[]
montant=0
while(True):    
    prix=int(input("Prix:"))
    if prix==0:
        break
    quantite=int(input("Quantité:"))
    designation=input("Désignation:")
    montant+=prix*quantite
    ## ajouter dans la liste principale
    principale.append((designation, prix*quantite))

## boucle d'affichage de principale
print("Facture")
for o in principale:
    print(f"- {o[0]} \t {o[1]}")
print(f"Montant = {montant}")
print("Montant =", montant)