import random as rdm

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "t", "v", "w", "x", "y", "z"]
ALPHABET=[]
for i in alphabet:
    ALPHABET+=i.upper()

def plaqueIm(ALPHABET):
    plaque=""
    for i in range(2):
        lettreAl=rdm.randint(0,21)
        lettre=ALPHABET[lettreAl]
        plaque+=lettre
    plaque+='-'

    for i in range(3):
        nbAl=rdm.randint(0,10)
        nb=str(nbAl)
        plaque+=nb
    plaque+='-'

    for i in range(2):
        lettreAl=rdm.randint(0,21)
        lettre=ALPHABET[lettreAl]
        plaque+=lettre

    return plaque

print(plaqueIm(ALPHABET))
