print("Supérette Alpha")
nombre_produit = int(input("Combien de produits dans le panier :"))

total=0
for i in range(nombre_produit):
    designation = input("Désignation :")
    prix = int(input("Prix:"))
    total +=prix

print("Total:", total)
somme_recu = int(input("Somme reçue:"))
print("A rendre:", somme_recu - total)