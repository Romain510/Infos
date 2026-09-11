nvlOp=True

while nvlOp:

    operation=input("Choississer le type d'opérations: '+','-','/' ou '*' \n")
    assert operation=='+' or operation=='-' or operation=='/' or operation=='*', "L'operateur doit être '+','-','/' ou '*'"

    nb1=int(input("Nombre 1 (numérateur): \n"))

    nb2=int(input("Nombre 2 (dénominateur): \n"))

    if operation=='/':
        assert nb2!=0 , "On ne peut pas diviser par 0."

    if operation=="+":
        resultat=nb1+nb2
    elif operation=="-":
        resultat=nb1-nb2
    elif operation=="/":
        resultat=nb1/nb2
    elif operation=="*":
        resultat=nb1*nb2
    else:
        print("L'operateur n'est pas pris en compte ou n'existe pas")

    print(f"Le resultat de l'operation {nb1}{operation}{nb2} est {resultat}")

    nvlOperation=str(input("Voulez vous effectuer une nouvelle opération?"))
    nvlOperation.lower()
    if nvlOperation=='o':
        nvlOp=True
    else:
        nvlOp=False