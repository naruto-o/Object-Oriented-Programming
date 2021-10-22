class Dad():
    basketball=1

class Son(Dad):
    dance = 1
    basketball = 6
    def isdance(self):
        return f"i can dance in {self.dance} forms"

class Grandson(Son):
    dance = 6
    guitar = 2
    def isdance(self):
        return f"Jackson yeah!Yes I dance very awesomely {self.dance} no of times"
    
darry = Dad()
larry = Son()
harry = Grandson()
print(harry.isdance())
print(harry.basketball)   # i did not mention basketball but son know basketball 6 so grndson inherited its 6 basketball
#print(darry.isdance())     #it will show a error because dad does not know how to dancew
print(darry.basketball)