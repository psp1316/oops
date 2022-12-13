


class Programmer:
    def details(self):
        print("language:",self.language)
        print("salary:",self.salary)

abhi=Programmer()
psp=Programmer()

abhi.language="c++"
abhi.salary="2 lakhs"

psp.language="python"
psp.salary="3 lakhs"

a=input("enter employee name: ")
if(a=="abhi"):
    abhi.details()
elif(a=="psp"):
    psp.details()
    
   

    