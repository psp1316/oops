



class Rectangle():
    

    # def __init__(self,l=0,b=0):
    #     self.l= l
    #     self.b=b

    def details(self):
        self.d=float(input("enter the lenght: "))
        self.c=float(input("enter the breadth: "))   

    def area(self):
     print("area of rectangle=",self.d*self.c)


blue=Rectangle()
blue.details() 
blue.area()





