panier=[]
print("Supérette Alpha")
#nombre_produit = int(input("Combien de produits dans le panier :"))

total=0
#for i in range(nombre_produit):
while(True):
    designation = input("Désignation :")
    if len(designation) == 0:
        break
    prix = int(input("Prix:"))
    quantite = int(input("Quantité:"))
    panier.append((designation, prix, quantite))
    total += prix*quantite

for elt in panier:
    print(f"{elt[0]} \t {elt[1]} \t {elt[2]}")

print("Total:", total)
while(True):
    somme_recu = int(input("Somme reçue:"))
    if somme_recu >= total:
        break
print("A rendre:", somme_recu - total)