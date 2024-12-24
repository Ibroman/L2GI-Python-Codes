A=B=C=0
while(True):
    nombre=input("Nombre:")
    A=B
    B=C
    C=int(nombre)
    if A<B and B<C:
        break