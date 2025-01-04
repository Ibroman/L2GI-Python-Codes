# Application : On réalise une fonction qui retourne les racines carées d'un polynome du 2nd dégré
# On doit saisir A, B, C
# On calcule Delta, X1, X2 et on retourne sous forme d'un tuple
# On utilise la bibliothèque "math"

from math import sqrt

def Polynome(x,y,z):
    Delta=y*y - 4*x*z
    if Delta>=0:
        X1=(-y-sqrt(Delta))/(2*x)
        X2=(-y+sqrt(Delta))/(2*x)
        return (Delta,X1,X2)
    else:
        return ()
    
A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
resultat=Polynome(A,B,C)
if (len(resultat) == 0):
    print("Aucune solution")
else:
    print(resultat)

