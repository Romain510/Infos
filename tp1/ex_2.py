listeNombre=[]

def creaListe(listeNombre):
    nombre=int(input("Entrer un entier"))
    while nombre>=0:
        listeNombre.append(nombre)
        nombre=int(input("Entrer un entier"))
    return listeNombre

def triCroissant(listeNombre):
    for nombre in range(len(listeNombre)):
        for balayage in range(len(listeNombre)-1):
            if listeNombre[nombre]<listeNombre[balayage]:
                listeNombre[balayage],listeNombre[nombre]=listeNombre[nombre],listeNombre[balayage]
    return listeNombre

def maxi(listeNombre):
    maximum=listeNombre[0]
    for nombre in listeNombre:
        if nombre>maximum:
            maximum=nombre
    return maximum

def mini(listeNombre):
    minimum=listeNombre[0]
    for nombre in listeNombre:
        if nombre<minimum:
            minimum=nombre
    return minimum

creaListe(listeNombre)
print("La liste est:",listeNombre)
print("La liste trié en ordre croissant est: ",triCroissant(listeNombre))
print("Le maximum de la liste est: ",maxi(listeNombre))
print("Le minimum de la liste est: ",mini(listeNombre))