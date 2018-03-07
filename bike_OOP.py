class Bike(object):
    miles = 0

    def __init__ (self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        
    def displayInfo(self):
        print(self.price) 
        print(self.max_speed)
        print(self.miles)
        return self

    def ride(self):
        print("Riding")
        self.miles = self.miles + 10
        return self
  
    def reverse(self):
        print("Reversing")
        self.miles = self.miles - 5
        if self.miles <= 0:
            self.miles = 0
        return self

bike1 = Bike(1500,"90mph",200)
bike2 = Bike(1200,"100mph",50)
bike3 = Bike(3200,"200mph",100)
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()



