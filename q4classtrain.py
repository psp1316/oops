class train():
    
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def seatsleft(self):
        print(f"Welcome to {self.name}")
        print(f"the fare of the train is  {self.fare}")
        print("seats available are ",self.seats)
    def book(self):
        self.a=int(input("how much seats you want"))
        print(f"your {self.a} seats are confirmed!!\n seats left are {self.seats-self.a}")  
        
a=train("rajhdhani express","500rs",50)   
a.seatsleft()
a.book()
