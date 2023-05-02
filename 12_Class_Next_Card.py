val_order = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
suit_order = ["club","diamond","heart","spade"]


class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        return "(%s %s)"%(self.value,self.suit)

    def next1(self):
        indval = val_order.index(self.value)
        indsuit = suit_order.index(self.suit)
        if indsuit == 3:
            indsuit = 0
            if indval == 12: indval = 0
            else: indval += 1
        else:
            indsuit += 1
        return Card(val_order[indval],suit_order[indsuit])

    def next2(self):
        indval = val_order.index(self.value)
        indsuit = suit_order.index(self.suit)
        if indsuit == 3:
            indsuit = 0
            if indval == 12: indval = 0
            else: indval += 1
        else:
            indsuit += 1
        self.value = val_order[indval]
        self.suit = suit_order[indsuit]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())
print("----------")

for i in range(n):
    print(cards[i])
print("----------")

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])