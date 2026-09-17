import random
n=int(input("Combien de valeur? (entre 2 et 100)\n"))
liste=[random.randint(0,500) for i in range(n)]
verif=True

while verif:
    for elem in liste:
        for i in range(len(liste)):
            if elem==i:
                verif=False
