class Isbn:
    def __init__(self, number):
        self.number = number

    def sumodd(self):
        sum = 0
        for i in range(1,len(self.number)-1,2):
            sum += 3*(int(self.number[i]))
        return sum

    def sumeven(self):
        sum = 0
        for i in range(len(self.number),2):
            sum += int(self.number[i])
        return sum

    def checksum(self):
        k = 10 - (self.sumodd() + self.sumeven())%10
        if k ==10:
            return 0
        else:
            return k

    def result(self):
        return self.number[0:len(self.number)] + str(self.checksum())

    def valid(self):
        if self.number == self.result():
            return True
        else:
            return False

if __name__ == '__main__':
     isbn = input("ISBN: ")
     isbn = Isbn(isbn)
     if isbn.valid():
         print("ISBN valid: ")
     else:
         print('ISBN not valid')
