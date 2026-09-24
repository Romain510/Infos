def factorielle(x):
    resultat=1
    for i in range(x):
        resultat=resultat*x
        x-=1
    return resultat