class Rectangle:
    def __init__(self, longueur, largeur, nom="rectangle"):
        self.longueur=longueur
        self.largeur=largeur
        self.nom=nom

    def air (self):
        return f"L'air du rectangle est de: {self.longueur * self.largeur}"

    def affichage (self):
        return f"Longueur: {self.longueur}, Largeur: {self.largeur}"

class Carre(Rectangle):
    def __init__(self, cote, nom="carre"):
        self.nom=nom
        super().__init__(longueur=cote, largeur=cote)





if __name__ == "__main__":
    rect=Rectangle(10,5,"rectangle")
    car=Carre(5,"carre")
    print(f"Taille du rectangle: \n {rect.affichage()}")
    print(f"Taille du carre: \n {car.affichage()}")
    
