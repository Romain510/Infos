from random import shuffle


class CardValue:
    def __init__(self, value_txt, value_pts):
        self.value_txt = value_txt
        self.value_pts = value_pts


class CardColor:
    def __init__(self, shade, shade_name, foreground_color, background_color):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color


class Card:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def is_equal_value(self, card):
        return self.valeur.value_pts == card.valeur.value_pts

    def __eq__(self, autre):
        return (self.valeur.value_pts == autre.valeur.value_pts
                and self.couleur.shade == autre.couleur.shade)

    def __hash__(self):
        return hash((self.valeur.value_pts, self.couleur.shade))

    def __lt__(self, autre):
        return self.valeur.value_pts < autre.valeur.value_pts

    def __gt__(self, autre):
        return self.valeur.value_pts > autre.valeur.value_pts

    def __le__(self, autre):
        return self.valeur.value_pts <= autre.valeur.value_pts

    def __ge__(self, autre):
        return self.valeur.value_pts >= autre.valeur.value_pts

    def __str__(self):
        c = self.couleur
        return f"{c.foreground_color}{c.background_color} {self.valeur.value_txt}{c.shade} \033[0m"

    def __repr__(self):
        return f"Card({self.valeur.value_txt!r}, {self.couleur.shade_name!r})"


VALEURS = [CardValue(str(i), i) for i in range(2, 11)] + [
    CardValue("J", 11),
    CardValue("Q", 12),
    CardValue("K", 13),
    CardValue("A", 14),
]

NOIR = "\033[30m"
ROUGE = "\033[31m"
FOND = "\033[47m"

COULEURS = [
    CardColor("♠", "pique", NOIR, FOND),
    CardColor("♣", "trèfle", NOIR, FOND),
    CardColor("♦", "carreau", ROUGE, FOND),
    CardColor("♥", "coeur", ROUGE, FOND),
]


class Deck:
    def __init__(self):
        self.cartes = [Card(v, c) for c in COULEURS for v in VALEURS]

    def melanger(self):
        shuffle(self.cartes)

    def tirer(self):
        if not self.cartes:
            raise IndexError("Le paquet est vide")
        return self.cartes.pop()

    def __len__(self):
        return len(self.cartes)

    def __str__(self):
        return " ".join(str(c) for c in self.cartes)


if __name__ == "__main__":
    c1 = Card(CardValue("K", 13), COULEURS[0])
    c2 = Card(CardValue("K", 13), COULEURS[2])
    c3 = Card(CardValue("5", 5), COULEURS[3])

    print("c1 =", c1)
    print("c2 =", c2)
    print("c3 =", c3)
    print("repr(c1) =", repr(c1))

    print("\n--- Comparaisons ---")
    print("c1.is_equal_value(c2) :", c1.is_equal_value(c2))
    print("c1.is_equal_value(c3) :", c1.is_equal_value(c3))
    print("c1 == c2 :", c1 == c2)
    print("c1 > c3  :", c1 > c3)
    print("c3 < c1  :", c3 < c1)
    print("c1 >= c2 :", c1 >= c2)

    print("\n--- Deck ---")
    d = Deck()
    print("Nombre de cartes :", len(d))
    d.melanger()
    print("Paquet mélangé :")
    print(d)
    main = [d.tirer() for _ in range(5)]
    print("\nMain de 5 cartes :", *main)
    print("Cartes restantes :", len(d))
    print("Meilleure carte :", max(main))