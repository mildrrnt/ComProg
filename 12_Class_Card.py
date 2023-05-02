class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(%s %s)"%(self.value.upper(),self.suit.lower())

    def getScore(self):
        if self.value == "A":
            return 1
        elif self.value in "JKQ":
            return 10
        else:
            return int(self.value)
        
    def sum(self,other):
        return (self.getScore()+other.getScore())%10
    
    def __lt__(self,rhs):
        val_order = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
        suit_order = ["club","diamond","heart","spade"]
        ind1val = val_order.index(self.value)
        ind2val = val_order.index(rhs.value)
        ind1suit = suit_order.index(self.suit)
        ind2suit = suit_order.index(rhs.suit)
        #compare value by value
        return (ind1val,ind1suit) < (ind2val,ind2suit)
    
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])