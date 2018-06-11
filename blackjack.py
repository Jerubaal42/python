from random import randint

def shuffle():
    global deck
    deck=[]
    for suit in range(0,4):
        for value in range(1,14):
            if(value<10):
                deck.append(value)
            else:
                deck.append(10)
    for tweak in range(0,10):
        deck.pop(randint(0,len(deck)-1))

def drawcard():
    global deck
    card=deck.pop(randint(0,len(deck)-1))
    return card

def round():
    global players
    global deck
    global playercard
    shuffle()
    dealercard=[]
    playerbet=[]
    for player in range(0,players):
        playercard[player].append(drawcard())
        playerbet[player].append([])
    dealercard.append(drawcard())
    print("Dealer: {0}".format(dealercard))
    for player in range(0,players):
        print("Player {0} has {1}".format(player,playercard[player]))

def game():
    global players
    global startmoney
    global playercard
    playermoney=[]
    playercard=[]
    for player in range(0,players):
        playermoney.append(startmoney)
        playercard.append(player)
    round()

if __name__=="__main__":
    global players
    global startmoney
    while True:
        try:
            players=(int(input("Number of Players: ")))
            if(players<1):
                raise ValueError
            else:
                break
        except:
            print("Invalid Input")
    while True:
        try:
            startmoney=(int(input("Starting Money: ")))
            if(startmoney<1):
                raise ValueError
            else:
                break
        except:
            print("Invalid Input")
    game()
