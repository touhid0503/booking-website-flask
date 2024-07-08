class a:
    def __init__(self) -> None:
        print("hi1")

    def j(self):
        print("hi2")


class b(a):  # inherit
    def __init__(self) -> None:
        super().__init__()
        print("hi3")
        
class c(b):  # multilevel inherit
    def __init__(self) -> None:
        super().__init__()
        print("hi4")

# pass

n = b()
n.j()
n= a()
n.j()
n=c()

