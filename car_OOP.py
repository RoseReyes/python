class Car(object):

    def __init__ (self,price,speed,fuel,mileage,tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax

toyota = Car(25000,"75mph","Full","15mpg",0)
honda = Car(20000,"80mph","Kinda of Full","32mpg",0)
wrangler = Car(27000,"100ph","Not Full","50mpg",0)
ferrari = Car(1500000,"400mph","Empty","60mpg",0)
mustang = Car(160000,"500mph","Empty","70mpg",0)
jaguar = Car(1700000,"600mph","Empty","80mpg",0)
        
