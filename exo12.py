class Rectangle:
    def __init__(self, L, l):
        self.longueur=L
        self.largeur=l
    def __str__(self):
        return "Je suis un rectangle de longueur " + str(self.longueur) + " et de largeur " + str(self.largeur)
    def Perimetre(self):
        return 2*(self.longueur+self.largeur)
    def Surface(self):
        return self.longueur*self.largeur


r1=Rectangle(50,20)
r2=Rectangle(30,10)
print(r1)
print("Surface: ", r1.Surface())
print("Perimetre: " + str(r1.Perimetre()))