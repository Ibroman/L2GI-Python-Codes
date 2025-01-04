# Application : On réalise une fonction qui retourne le plus nombre des trois passés en paramètre

def plusgrand(x,y,z):
    if x>=y and x>=z:
        pg=x
    elif y>=x and y>=z:
        pg=y
    else:
        pg=z
    return pg

print("Plus grand:", plusgrand(10,50,20))
print("Plus grand:", plusgrand(100,100,20))