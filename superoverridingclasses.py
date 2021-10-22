class A:
    classvar1 = "i am a class variable in a"
    def __init__(self):
        self.var1 = "i am in side class a constructor"
        self.classvar1 = "instance var in class a"
        self.special="special"

class B(A):                           #this class is overriding everything from class a so to remove this we use super
    classvar1 = "i am in class b"
    def __init__(self):
        super().__init__()          #this is used to acces the class a by bypassing the ovewrride 
        self.var1 = "i am in class b"
        self.classvar1="instance var in class b"
a = A()
b=B()
       
       
print(b.var1,b.special)
