# Application : On réalise la saisie des achats du panier d'un client
# on stocke dans une "list" la désignation et la montant pour chaque produit acheté
# à la fin de la saisie on affiche l'historique des achats et affiche le montant à payer

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