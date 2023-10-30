class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __normalise(self):
        if self.denominator < 0:
            self.__numerator = -self.numerator
            self.__denominator = abs(self.denominator)

        a = abs(self.numerator)
        b = self.denominator

        while a != 0:
            a, b = b % a, a

        nod = b
        self.__numerator //= nod
        self.__denominator //= nod

    def __mul__(self, num: 'Rational'):
        return Rational(self.numerator * num.numerator, self.denominator * num.denominator)

    def __truediv__(self, num: 'Rational'):
        return Rational(self.numerator * num.denominator, self.denominator * num.numerator)

    def __add__(self, num: 'Rational'):
        return Rational(self.numerator * num.denominator + num.numerator * self.denominator,
                        self.denominator * num.denominator)

    def __sub__(self, num: 'Rational'):
        return Rational(self.numerator * num.denominator - num.numerator * self.denominator,
                        self.denominator * num.denominator)

    def __gt__(self, num: 'Rational'):
        return self.numerator / self.denominator > num.numerator / num.denominator

    def __lt__(self, num: 'Rational'):
        return self.numerator / self.denominator < num.numerator / num.denominator

    def __ge__(self, num: 'Rational'):
        return self.numerator / self.denominator >= num.numerator / num.denominator

    def __le__(self, num: 'Rational'):
        return self.numerator / self.denominator <= num.numerator / num.denominator

    def __eq__(self, num: 'Rational'):
        return self.numerator / self.denominator == num.numerator / num.denominator

    def __ne__(self, num: 'Rational'):
        return self.numerator / self.denominator != num.numerator / num.denominator


if __name__ == '__main__':
    rational = Rational(2, 3)
    assert rational.numerator == 2
    assert rational.denominator == 3
    assert str(rational * Rational(1, 2)) == '1/3'
    assert str(rational / Rational(3, 4)) == '8/9'
    assert str(rational + Rational(2, 5)) == '16/15'
    assert str(rational - Rational(3, 4)) == '-1/12'
    assert Rational(3, 4) > Rational(1, 2)
    assert Rational(2, 3) < Rational(4, 5)
    assert Rational(1, 4) >= Rational(1, 6)
    assert Rational(2, 5) >= Rational(2, 5)
    assert Rational(1, 12) <= Rational(1, 3)
    assert Rational(2, 7) <= Rational(2, 7)
    assert Rational(3, 5) == Rational(3, 5)
    assert Rational(1, 2) != Rational(-1, 2)
    assert str(Rational(1, 4) * (Rational(3, 2)
                                 + Rational(1, 8))
               + Rational(156, 100)) == '1573/800'


