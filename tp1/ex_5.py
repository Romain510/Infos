resultat=""
q=int(input("Nombre à convertir"))
while q>0:
    reste=q%2
    resteStr=str(reste)
    resultat+=resteStr
    q=q//2
    

print(resultat)