from math import sqrt

A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
Delta=B*B - 4*A*C
if Delta>=0:
    X1=(-B-sqrt(Delta))/(2*A)
    X2=(-B+sqrt(Delta))/(2*A)
    print("X1=",X1)
    print("X2=",X2)
else:
    print("Aucune solution")