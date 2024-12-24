class Produit:
    def __init__(self, des, prix, qu):
        self.designation=des
        self.prix=prix
        self.quantite=qu

    def __str__(self):
        return f"Désignation:{self.designation}\tPrix:{self.prix}\tQuantité:{self.quantite}"
    
    def getMontant(self):
        return self.prix*self.quantite
    
p1=Produit("Lait", 200,5)
p2=Produit("Riz", 500,3)
p3=Produit("Ananas", 700,4)
print(p1)
print(p2)
print(p3)
montant=p1.getMontant()+p2.getMontant()+p3.getMontant()
print("Montant=", montant)