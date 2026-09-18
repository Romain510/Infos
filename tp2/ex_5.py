polynome_1=[10,5,3,4,2]
polynome_2=[2,4,20,4]
x=2

def fonction(polynome):
    coef=int(input("Coefficient: \n"))
    polynome.insert(0,coef)
    return polynome

def saisiePoly():
    polynome=[]
    puissance=int(input("Quel puissance du polynome?: \n"))
    for i in range(puissance):
        valeur=int(input(f"Saisir le coef de x à la puissance {puissance-i} du polynome:\n"))
        polynome.append(valeur)
    valeur=int(input(f"Saisir la valeur finale:\n"))
    polynome.append(valeur)
    return polynome


def affichePoly(polynome):
    strPoly=""
    for coef in range(len(polynome)-1):
        strPoly+=str(polynome[coef])+"x^"+str((len(polynome)-1)-coef)+"+"

    strPoly+=str(polynome[-1])
    return strPoly

def suppPoly(polynome):
    polynome.clear()

def addPoly(polynome_1, polynome_2):
    sommePoly=[]
    if len(polynome_2)>len(polynome_1):
        for element in range(len(polynome_2)-len(polynome_1)):
             sommePoly.append(polynome_2[element])
        for element in range(len(polynome_1)):
            sommePoly.append(polynome_1[element]+polynome_2[element+1])
    elif len(polynome_1)>len(polynome_2):
            for element in range(len(polynome_1)-len(polynome_2)):
                sommePoly.append(polynome_1[element])
            for element in range(len(polynome_2)):
                sommePoly.append(polynome_2[element]+polynome_1[element+1])
    elif len(polynome_2)==len(polynome_1):
            for element in range(len(polynome_1)):
                sommePoly.append(polynome_1[element]+polynome_2[element])
    return sommePoly

def multPoly(polynome_1,x):
    produitPoly=[]
    for element in polynome_1:
        produitPoly.append(element * x)

    return produitPoly

print(multPoly(polynome_1,x))