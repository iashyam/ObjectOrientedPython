class Password:
    def __init__(self, password):
        self.password = password

    def lenth(self):
        if len(self.password) >= 8:
            return True
        return False

    def digit(self):
        return self.password.isalnum()

    def numm(self):
        count  = 0
        for i in range(0,10):
            if str(i) in self.password:
                count += self.password.count(str(i))

        if count >=2:
            return True

    def IsValid(self):
        return self.lenth() and self.digit() and self.numm()

    def printError(self):
        if not self.lenth():
            print("Password length is minimmun 8!")
        elif not self.digit():
            print("Password should atleast contain two numbers!\n"
                  "And there should not be any special characters!")
        elif not self.numm():
            print('Password should atleast contain two numbers!')
        else:
            pass




if __name__ == '__main__':
    password = input("Enter Password: ")
    password = Password(password)
    while not password.IsValid():
        if password.IsValid():
            print("The Password is Valid!")
            break
        else:
            print("The password is invalid!")
            password.printError()

        password = input("Enter Password Again: ")
        password = Password(password)

    print("The Password is Valid!")