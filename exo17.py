class CompteBancaire:
    def __init__(self, n : str, s : int):
        self.nom = n
        self.solde = s
        self.operations = []

    def Crediter(self, m):
        self.solde +=m
        self.operations.append(f"Compte crédité de {m}. Solde = {self.solde}.")

    def Debiter(self, m):
        if self.solde >= m:
            self.solde -=m
            self.operations.append(f"Compte débité de {m}. Solde = {self.solde}.")
        else:
            print("Solde insuffisant")
    
    def getSolde(self):
        return self.solde
    
    def __str__(self):
        return f"{self.nom} a pour solde {self.solde} DJF."
    
    def getHistorique(self):
        return "\n".join(self.operations)

c = CompteBancaire("Mohamed", 1000)
c.Crediter(2000)
c.Debiter(500)
c.Debiter(5000)
print(str(c.getSolde()))
print(c.getHistorique())