class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal's Health:",self.health
        return self

class Dog(Animal):
    def __init__(self,health):
        self.health = 150

    def walk(self):
        #call the parent method run() to deduct health, -1
        return super(Dog,self).walk()

    def run(self):
        #call the parent method of run() to deduct health, -5
        return super(Dog,self).run()

    def displayHealth(self):
        print "I'm a dog."
        print "Health now is:",self.health
        return self

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,health):
        self.health = 170

    def walk(self):
        #call the parent method run() to deduct health, -1
        return super(Dragon,self).walk()

    def run(self):
        #call the parent method of run() to deduct health, -5
        return super(Dragon,self).run()

    def displayHealth(self):
        print "I am a dragon!"
        return super(Dragon,self).displayHealth()

    def fly(self):
        self.health -= 10
        return self

class Garfield(Animal):
    def __init__(self,health):
        self.health = 60

    def walk(self):
        #call the parent method run() to deduct health, -1
        return super(Garfield,self).walk()

    def run(self):
        #call the parent method of run() to deduct health, -5
        return super(Garfield,self).run()

    def displayHealth(self):
        return super(Garfield,self).displayHealth()

#This is an instance of the class  
myDog = Dog(0)
dannyDragon = Dragon(0)
cat = Garfield(0)
myDog.walk().walk().walk().run().run().pet().fly().displayHealth()
dannyDragon.fly().walk().displayHealth()
cat.fly().pet().displayHealth()
