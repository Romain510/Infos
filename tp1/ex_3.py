ageHumain=int(input("Entrer votre âge humain: "))
ageCanin=0
for annee in range(ageHumain):
    if annee <2:
        ageCanin+=10.5
    else:
        ageCanin+=4

print(ageCanin)