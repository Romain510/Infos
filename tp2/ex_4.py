listeScore=[]
run=True

while run:
    score=input("Choix: x, 'D', 'C', '+' \n")

    if score.lower()=='d' or score.lower()=='c' or score.lower()=='+':
        if score.lower()=="c":
            if listeScore==[]:
                print("Pas de score précédent")
            else:
                del listeScore[-1]
        elif score.lower()=="d":
            if listeScore==[]:
                print("Pas de score précédent")
            else:
                listeScore.append(int(listeScore[-1]) * 2)
        elif score.lower()=="+":
            if listeScore==[]:
                print("Pas de score précédent")
            else:
                sommeScore=int(listeScore[-1])+int(listeScore[-2])
                listeScore.append(sommeScore)
    else:
        listeScore.append(score)

    print(listeScore)

    continuer=input("Continuer? o/n \n")
    if continuer.lower()=="n":
        run=False

    

scoreFinal=0
for element in listeScore:
    scoreFinal+=int(element)

print("Score final: ", scoreFinal)