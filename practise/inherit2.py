#multiple inh
class a:
    def h(self):
        print("hi")

class b:
    def k(self):
        print("hi2")

class c(a,b):
    pass

n=c()
n.h()
n.k()

