class a: #class defined
    def __init__(self): #constructor 
        # print("hi");
        print(self.name) #self means this like this.name
        # pass
    name="touhid"; #attribute

n=a(); #object create
print(n.name) #access

class b:
    # name="K" 
    def __init__(this,name): #para const
        print("creating...")
        this.name=name;    
    def fun(this,num): #method
        this.num=num;
        print("function",num)
z=b("Touhid")
print(z.name)
z=b("m")
print(z.name)
z.fun(0)
print(z.num)

class jk:
    @staticmethod
    def fun():
        print(10)    
h= jk()
h.fun();
jk.fun() 