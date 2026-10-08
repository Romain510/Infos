from math import gcd


class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être nul")
        if den < 0:
            num, den = -num, -den
        d = gcd(num, den)
        self.num = num // d
        self.den = den // d

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __add__(self, autre):
        n = self.num * autre.den + autre.num * self.den
        d = self.den * autre.den
        return Fraction(n, d)

    def __sub__(self, autre):
        n = self.num * autre.den - autre.num * self.den
        d = self.den * autre.den
        return Fraction(n, d)

    def __mul__(self, autre):
        return Fraction(self.num * autre.num, self.den * autre.den)

    def __truediv__(self, autre):
        if autre.num == 0:
            raise ZeroDivisionError("Division par une fraction nulle")
        return Fraction(self.num * autre.den, self.den * autre.num)

    def __gt__(self, autre):
        return self.num * autre.den > autre.num * self.den

    def __lt__(self, autre):
        return self.num * autre.den < autre.num * self.den

    def __ge__(self, autre):
        return self.num * autre.den >= autre.num * self.den

    def __le__(self, autre):
        return self.num * autre.den <= autre.num * self.den

    def __eq__(self, autre):
        return self.num == autre.num and self.den == autre.den

    def __ne__(self, autre):
        return not self == autre


if __name__ == "__main__":
    a = Fraction(1, 2)
    b = Fraction(3, 4)

    print("a =", a)
    print("b =", b)

    print("\n--- Opérations ---")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)

    print("\n--- Comparaisons ---")
    print("a > b  :", a > b)
    print("a < b  :", a < b)
    print("a >= b :", a >= b)
    print("a <= b :", a <= b)
    print("a == b :", a == b)
    print("a != b :", a != b)

    print("\n--- Cas particuliers ---")
    c = Fraction(2, 4)
    print("2/4 se simplifie en :", c)
    print("1/2 == 2/4 :", a == c)
    print("1/-3 devient :", Fraction(1, -3))
    print("1/2 + 1/2 =", a + a)