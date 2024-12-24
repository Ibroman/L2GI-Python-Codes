# Créer une classe Produit :
# Attributs : designation, prix, quantite
# Méthodes : __init__, __str__, getRemise, getMontant
# Tests :
# - 4 objets produits et les ajouter à une liste
# - calculer la somme des remises et l'afficher
# - calculer somme des montants et l'afficher

class Produit:
    def __init__(self, des, prix, qu):
        self.designation=des
        self.prix=prix
        self.quantite=qu

    def __str__(self):
        return f"Désignation:{self.designation}\tPrix:{self.prix}\tQuantité:{self.quantite}\tRemise:{self.getRemise()}\tMontant:{self.getMontant()}"
    
    def getRemise(self):
        total = self.prix*self.quantite
        if total>=10000 and self.quantite>=5:
            return self.prix + total * 0.1
        elif total>=5000 and self.quantite>=5:
            return self.prix
        elif total>=10000:
            return total * 0.1
        else:
            return 0
    
    def getMontant(self):
        return self.prix*self.quantite - self.getRemise()
    
p1=Produit("Lait", 2000,3)
p2=Produit("Riz", 1000,7)
p3=Produit("Ananas", 2000,7)
p4=Produit("BlaBla", 4000,4)
print(p1)
print(p2)
print(p3)
print(p4)

panier=list()
panier.append(p1)
panier.append(p2)
panier.append(p3)
panier.append(p4)
remise=montant=0
for p in panier:
    remise += p.getRemise()
    montant += p.getMontant()
print("Remise=", remise)
print("Montant=", montant)