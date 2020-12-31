import math

class Circle:

    #defining the attributes
    def __init__(self, radius):
        self.radius = radius

    #defining the methods
    def getCircumfrance(self):
        return 2*self.radius*math.pi

    def getArea(self):
        return math.pi*self.radius**2


#Ye ban gyi apni Circle Class

if __name__ == '__main__':

    c1 = Circle(5)
    c2 = Circle(6)

    print({c1.getArea()})
