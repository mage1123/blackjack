
import random

class Cards():
    instances = []
    def __init__(self, cardtype, cardvalue):
        self.cardtype = cardtype
        self.cardvalue = cardvalue
    def maths(self):
        return self.cardvalue
    def ischosen(self):
    	PlayerHand.append(self.cardtype + " " + self.cardvalue)
    	PlayerHand.append(self.cardvalue)

PlayerHand = []

def CardPickPlayer():
	CardValue = random.randint(1,2)
	CardType = random.randint(1, 2)
	if CardValue == 1 and CardType == 1:
		ClubsAce.ischosen()
	print(PlayerHand)




#Set card values
    
ClubsAce = Cards("Clubs", "1")
DiamondsAce = Cards("Diamonds", "1")
HeartsAce = Cards("Hearts", "1")
SpadesAce = Cards("Spades", "1")

ClubsTwo = Cards("Clubs", "2")
DiamondsTwo = Cards("Diamonds", "2")
HeartsTwo = Cards("Hearts", "2")
SpadesTwo = Cards("Spades", "2")

ClubsThree = Cards("Clubs", "3",)
DiamondsThree = Cards("Clubs", "3")
HeartsThree = Cards("Clubs", "3")
SpadesThree = Cards("Clubs", "3")

ClubsFour = Cards("Clubs", "4")
DiamondsFour = Cards("Diamonds", "4")
HeartsFour = Cards("Hearts", "4")
SpadesFour = Cards("Spades", "4")

ClubsFive = Cards("Clubs", "5")
DiamondsFive = Cards("Diamonds", "5")
HeartsFive = Cards("Hearts", "5")
SpadesFive = Cards("Spades", "5")

ClubsSix = Cards("Clubs", "6")
DiamondsSix = Cards("Diamonds", "6")
HeartsSix = Cards("Hearts", "6")
SpadesSix = Cards("Spades", "6")

ClubsSeven = Cards("Clubs", "7")
DiamondsSeven = Cards("Diamonds", "7")
HeartsSeven = Cards("Hearts", "7")
SpadesSeven = Cards("Spades", "7")

ClubsEight = Cards("Clubs", "8")
DiamondsEight = Cards("Diamonds", "8")
HeartsEight = Cards("Hearts", "8")
SpadesEight = Cards("Spades", "8")

ClubsNine = Cards("Clubs", "9")
DiamondsNine = Cards("Diamonds", "9")
HeartsNine = Cards("Hearts", "9")
SpadesNine = Cards("Spades", "9")

ClubsTen = Cards("Clubs", "10")
DiamondsTen = Cards("Diamonds", "10")
HeartsTen = Cards("Hearts", "10")
SpadesTen = Cards("Spades", "10")

ClubsJack = Cards("Clubs", "10")
DiamondsJack = Cards("Diamonds", "10")
HeartsJack = Cards("Hearts", "10")
SpadesJack = Cards("Spades", "10")

ClubsQueen = Cards("Clubs", "10")
DiamondsQueen = Cards("Diamonds", "10")
HeartsQueen = Cards("Hearts", "10")
SpadesQueen = Cards("Spades", "10")

ClubsKing = Cards("Clubs", "10")
DiamondsKing = Cards("Diamonds", "10")
HeartsKing = Cards("Hearts", "10")
SpadesKing = Cards("Spades", "10")



CardPickPlayer()

"""
print(5 + int(ClubsTen.maths()))
"""



