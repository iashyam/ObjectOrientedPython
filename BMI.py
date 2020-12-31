class BMI:

    mpi = 0.01

    def __init__(self, name,age,weight, height):
        self.__name =  name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        return (self.__weight)/(self.__height*BMI.mpi)**2

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return 'Underweight'
        elif bmi <25:
            return 'Normal'
        elif bmi<30:
            return 'Overweight'
        else:
            return "Obese"

    def getAge(self):
        return self.__age

if __name__ == '__main__':
    shyam = BMI('Shyam','17',50,163.66)

    print(shyam.getAge())
    print(shyam.getBMI())
    print(shyam.getStatus())
