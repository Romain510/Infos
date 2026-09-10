approx=int(input("Entrer le nombre d'approximation de Pi: "))
nbQ=2
pi=3
signe=1

for i in range(approx):
    if signe==1:
        pi+=4/((nbQ)*(nbQ+1)*(nbQ+2))
    else :
        pi-=4/((nbQ)*(nbQ+1)*(nbQ+2))

    if signe==1:
        signe=2
    else :
        signe=1

    nbQ+=2

    print(pi)