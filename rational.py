def gg(a, b):
    gcd = 1
    k = 1
    while k <= a and k <= b:
        if a % k == 0 and b % k == 0:
            gcd = k
        k += 1
    return gcd


class Rational:
    def __init__(self,numerator = 0, denominator =1):
        gcd = gg(numerator, denominator)
        self.a = int(numerator/gcd)
        self.b = int(denominator/gcd)

    def __repr__(self):
        return str(self.a) + '/' + str(self.b)

    def __add__(self, other):
        return Rational((other.b*self.a + other.a * self.b),(self.b*other.b))

    def __sub__(self, other):
        return Rational((other.b*self.a - other.a * self.b),(self.b*other.b))

    def __mul__(self, other):
        return Rational(self.a*other.a, self.b * other.b)

    def __truediv__(self, other):
        return Rational(self.a*other.b, self.b * other.a)

    def __pow__(self, power, modulo=None):
        return Rational(self.a.__pow__(power),self.b.__pow__(power))

    def __invert__(self):
        return Rational(self.b, self.a)

    def __neg__(self):
        return Rational(-1*self.a , self.b)



if __name__ == '__main__':
    a = Rational(2,3)
    b = Rational(3,4)
    print( a ,'+',b, ' = ',a+b)
    print(a, '-', b, ' = ', a - b)
    print(a, 'x', b, ' = ', a * b)
    print(a, '/', b, ' = ', a / b)
    print('(',a,')', '^2' ' = ', a**2)
    print('-',a, '=', -a)
    print('inverse of ', a ,'=', ~a)