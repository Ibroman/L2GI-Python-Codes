from math import pi

class Cercle:
    def __init__(self, r):
        self.rayon=r

    def __str__(self):
        return "Je suis un cercle de rayon " + str(self.rayon)
    
    def Perimetre(self):
        return 2*pi*self.rayon
    
    def Surface(self):
        return pi*self.rayon*self.rayon

#c1=Cercle(50)
#c2=Cercle(30)
#print(c1)
#print("Surface: " + str(c1.Surface()))
#print("Perimetre: " + str(c1.Perimetre()))