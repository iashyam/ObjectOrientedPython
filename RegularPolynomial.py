from math import tan, pi

class regularploynonial:

    def __init__(self ,n,s,x,y):
        self.__n = n #number of sides
        self.__s = s #length of one side
        self.__x = x #x-coordinate of the center of ploynomial
        self.__y = y #y-coordinates of the center

    def getParameter(self):
        return self.__n * self.__s

    def getArea(self):
        return (self.__n * self.__s**2)/(4*tan(pi/self.__n))


if __name__ == '__main__':
    Poly1 = regularploynonial(6,4,3,4)

    print(Poly1.getArea())