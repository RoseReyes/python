import random
class Card(object):
    def __init__ (self,value):
        self.value = value
        
class Deck(object):
    def __init__ (self):
        cardList = []
        self.cardList = cardList
        for x in range(0,52):
            card = Card(200)
            self.cardList.append(card)

    def shuffle(self):
        print random.shuffle(self.cards)
    
    def displayValue(self):
        for y in range(0,len(self.cardList)):
            print self.cardList[y].value
        return self

    def draw(self):
        returnCard = self.cardList.pop()
        print returnCard.value
        return self

deck1 = Deck()
deck1.draw().displayValue()
    