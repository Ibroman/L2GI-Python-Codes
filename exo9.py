# Application : On réalise une fonction qui reçoit un tuple en paramètre
# qui parcourt les valeurs du tuple et les ajoute à une "list" s'il sont positifs

def positif(nombres):
    resultat=[]
    for x in nombres:
        if x>=0:
            resultat.append(x)
    return resultat


x=positif((-15,-8,10,20,230))
print(x)
