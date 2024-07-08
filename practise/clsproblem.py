class a:
    def __init__(self, accno, balance) -> None:
        # pass
        self.accno = accno
        self.balance = balance
        # print()

    def credit(self, amonut):
        self.balance += amonut
        print(self.get())

    # def debit():
    def debit(self, amonut):
        self.balance -= amonut
        print(self.get())

    def get(self):
        return self.balance


n = a(141, 550)
print(n.get())
n.debit(140)
n.credit(150)
z = a(124, 6400)
z.credit(1450)
z.debit(1654)


class abc:
    __p = 1

    def __init__(self, passw) -> None:
        # pass
        self.__passw = passw

    def hi(self, p):
        self.__p = p

    def __fun(self):
        print("private func")

    def fun1(self):
        self.__fun()

    def printed(self):
        print(self.__passw)

    def printed1(self):
        print(self.__p)

    # def setpass(self,pass):


obj1 = abc(123)
obj1.printed()
obj1.hi(14.5)
obj1.printed1()
obj1.fun1()

# print(obj1.passw) #can't access private
