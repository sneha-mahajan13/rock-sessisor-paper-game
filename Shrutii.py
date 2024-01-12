class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBikes(self):
        print("Total Bikes",self.stock)
    def rentforBikes(self,q):

        if q<=0:
            print("Enter the positive value or greater than zero ")
        elif q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("Total Price",q*100)
            print("Total Bikes",self.stock)
while True:
    object=BikeShop(100)
    Uc=int(input('''
    1 Display stocks
    2 Rent a Bike
    3 Exit
                  '''))                
    if Uc==1:
        object.displayBikes()
    elif Uc==2:
        n=int(input("Enter the quantity:-"))
        object.rentforBikes(n) 
    else:
        break      