class Produit:
    def __init__(self, des, prix, qu):
        self.designation=des
        self.prix=prix
        self.quantite=qu

    def __str__(self):
        return f"Désignation:{self.designation}\tPrix:{self.prix}\tQuantité:{self.quantite}\tRemise:{self.getRemise()}"
    def getPrix(self):
        return self.prix
    def getQuantite(self):
        return self.quantite
    def getRemise(self):
        if self.prix*self.quantite <5000:
            remise=0
        elif self.prix*self.quantite <10000:
            remise=self.prix*self.quantite*0.05
        else:
            remise=self.prix*self.quantite*0.1
        return remise
    def getMontant(self):
        return self.prix*self.quantite - self.getRemise()
    
class Panier:
    def __init__(self):
        self.panier = []
    def AjouterProduit(self, p):
        self.panier.append(p)

    def __str__(self):
        return "\n".join(self.panier)

    def AfficherFacture(self):
        mf=0
        for p in self.panier:
            print(p)
            mf += p.getMontant()
        print(f"Total: {mf} DJF.")

pan=Panier()
p1=Produit("Riz", 2000, 10)
p2=Produit("Lait", 1000, 6)
p3=Produit("Haricot", 500,4)
pan.AjouterProduit(p1)
pan.AjouterProduit(p2)
pan.AjouterProduit(p3)
pan.AfficherFacture()