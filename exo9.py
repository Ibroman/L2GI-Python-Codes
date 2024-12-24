def positif(nombres):
    resultat=[]
    for x in nombres:
        if x>=0:
            resultat.append(x)
    return resultat


x=positif((-15,-8,10,20,230))
print(x)
