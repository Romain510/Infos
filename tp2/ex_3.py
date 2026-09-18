import random
n=int(input("Combien de valeur? (entre 2 et 100)\n"))
liste=[random.randint(0,500) for i in range(n)]
verif=True
run=True

while verif and run:
    for elem in liste:
        for i in range(len(liste)):
            if elem==i:
                verif=False
    run=False

if not verif:
    print("Valeurs similaire détectée")
else:
    print("Aucune valeurs similaire détectée")

print(liste)
