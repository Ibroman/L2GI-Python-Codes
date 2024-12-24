from exo13 import Cercle
from exo12 import Rectangle

r1=Rectangle(50,20)
r2=Rectangle(30,10)
c1=Cercle(50)
c2=Cercle(30)
figures=[]
figures.append(r1)
figures.append(r2)
figures.append(c1)
figures.append(c2)
for f in figures:
    print(f)
    print("Surface: " + str(f.Surface()))
    print("Perimetre: " + str(f.Perimetre()))