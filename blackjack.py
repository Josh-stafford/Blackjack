from random import randint as rand
from math import floor

deck = 52
cardsPlayed = []
players = []
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
names = ["The dealer", "The player"]
dBust = False
end = False
bet = 0

class player:
    def __init__(this, score, currency, name):
        this.score = score
        this.currency = currency
        this.name = name


def Setup():
    global bet
    print("Setting up.")
    for i in range(0,2):
        players.append(player(0, 100, names[i]))
    print("You have started with", players[1].currency, "credits.")
    bet = Bet()
    players[1].currency = players[1].currency - bet
    Main()

def Bet():
    if players[1].currency != 0:
        currentBet = int(input("\nPlace your bet:\n> "))
        if currentBet <= players[1].currency and currentBet > 0:
            return currentBet
        else:
            print("You do not have enough credits to place that bet.")
            Bet()
    else:
        print("You are out of credits.")
        exit()


def Deal():
    cardNum=rand(1,52)
    print(cardNum)
    cardVal = cardNum%13
    if cardVal == 0:
        cardVal = 13
    if cardVal > 10 or cardVal == 1:
        cardVal = 11
    if cardNum/13 >= 1:
        suit = suits[floor(cardNum/13)]
    else:
        suit = suits[0]
    card = [cardNum, cardVal, suit]
    return card

def Main():
    global bet
    print("\nYou have", players[1].currency, "credits with a total score of", players[1].score)
    choice = input("Stick or twist?\n> ").upper()
    if choice == "TWIST":
        Play()
    elif choice == "STICK":
        highest = 0
        highestPlayer = ""
        print("You stuck.")
        for player in players:
            if player.score > highest:
                highest = player.score
                highestPlayer = player
        finish(highestPlayer)
        bet = Bet()
        players[1].currency = players[1].currency - bet
        Main()
    else:
        print("That is an invalid play. Try again.")
        Main()


def finish(name):
    global bet
    global cardsPlayed
    print("The current bet is", bet)
    pName = name.name
    if name.score > 21:
        print("_____________________\n")
        print(pName + " has gone bust.\nThank you for playing.")
        print("_____________________\n\n")
    else:
        print(pName + " wins with a score of", name.score)
    if players[1].score > players[0].score and players[1].score <=21 or players[0].score > 21:
        players[1].currency = players[1].currency + bet*2
        print("Your balance is now", players[1].currency, "credits.")
    elif players[0].score > players[1].score and players[0].score <= 21 or players[1].score > 21:
        print("You have lost", bet, "credits. You now have a balance of", players[1].currency, "credits.")
    for i in range(0,2):
        players[i].score = 0
        cardsPlayed = []


def Play():
    global cardsPlayed
    global dBust
    global bet
    dBust = False
    for player in range(0, 2):
        if dBust == False:
            newCard = Deal()
            while newCard in cardsPlayed:
                newCard = Deal()
            cardsPlayed.append(newCard)
            if player == 1:
                print("You have been dealt the", newCard[1], "of " + newCard[2])
            players[player].score = players[player].score + newCard[1]
            if players[player].score > 21:
                if player == 0:
                    dBust = True
                finish(players[player])
                bet = Bet()
                print(bet)
                players[1].currency = players[1].currency - bet
                Main()
    Main()


Setup()
