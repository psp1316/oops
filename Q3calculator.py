import math
class calculator:
    def __init__(self, a):
        self.a = a

    def square(self):
        print("square is: ", self.a*self.a)

    def cube(self):
        print("cube is: ", self.a*self.a*self.a)

    def squareroot(self):
        print("square root is: ", math.sqrt(self.a))

    @staticmethod
    def greet():
        print("***hey welcome here***")    

a=calculator(1)
a.greet()
a = calculator(int(input("enter the number\n")))
b = input("choose!what you want (A)square (B)squareroot (c)cube\n")

if(b == "square"):
    a.square()
elif(b == "squareroot"):
    a.squareroot()
else:
    a.cube()
