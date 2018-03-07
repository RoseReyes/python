class Product(object):

    def __init__ (self,Price,Item_Name,Weight,Brand,Status,Tax,Return):
        self.Price = Price
        self.Item_Name = Item_Name
        self.Weight = Weight
        self.Brand = Brand
        self.Status = "Sale"
        self.Tax = Tax
        self.Return = Return

    def sell(self):
        self.Status = "Sold"
        return self

    def addTax(self):
        self.Tax = self.Tax
        self.Price = self.Price + self.Tax
        return self

    def returnItem(self):
        if self.Return == "defective":
            self.Status = "defective"
            self.Price = 0
        elif self.Return == "new":
            self.Status = "Sale"
        elif self.Return == "open":
            self.Status = "used"
            self.Price = self.Price * 0.2
        return self

    def displayInfo(self):
        print "Price:", self.Price
        print "Item_Name:", self.Item_Name
        print "Weight:", self.Weight
        print "Brand:", self.Brand
        print "Status:", self.Status
        print "\n"

firstItem = Product(500.00,"Wrench","2.10lb","Co.XYZ","",12.5,"open")
secondItem = Product(100.00,"Hammer","3.10lb","Co.ABC","",8.00,"")
secondItem.sell().addTax().displayInfo()


        
