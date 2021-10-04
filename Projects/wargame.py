import random
#N: shuffledDeck
#P: generate a deck (list) of 52 shuffled cards to play the game with
#I: none
#R: standardDeck
def shuffledDeck():
  standardDeck = list(range(2, 15)) * 4
  random.shuffle(standardDeck)
  return standardDeck

print("Welcome to the Game : WAR!")
player1 = input("Input Player 1 name:")
player2 = input("Input Player 2 name:")
#N: playerTurn
#P: deal 1 card to a player
#I: playerName
#R: dealtCard
deck = shuffledDeck() 
print("The deck is" , deck) 

def gameWar():
   p1score = 0
   p2score = 0
   while len(deck) > 0:
    print("The cards will now be dealt for player 1 and player 2.")
    p1Card = (deck.pop())
    p2Card = (deck.pop())
    print("Player" , player1 ,"got the card" , p1Card)
    print("Player" , player2 ,"got the card" , p2Card)
    if p1Card == p2Card:
      print("WAR!")
      p1Card = (deck.pop())
      p2Card = (deck.pop())
      if p1Card > p2Card:
       p1score += 2
       print("Player" , player1 , "wins this round!\n ")
      if p2Card > p1Card:
       p2score += 2
       print("Player" , player2 , "wins this round!\n ")
    if p1Card > p2Card:
     p1score += 2
     print("Player" , player1 , "wins this round!\n")
     print("Score - [Player" , player1 , p1score , ": Player" , player2 , p2score , "]")
    if p2Card > p1Card:
     p2score += 2
     print("Player" , player2 , "wins this round!\n ")
     print("Score - [Player" , player1 , p1score , ": Player" , player2 , p2score , "]")
    if len(deck) == 0:
      print("Final score - [Player" , player1 , p1score , ": Player" , player2 , p2score , "]")
      if p1score > p2score:
        print("Player" , player1 , "wins")
      if p2score > p1score:
        print("Player" , player1 , "wins")
      if p1score == p2score:
        print("The game is a TIE!")
      print("All cards have been dealt!")

cardDrew = gameWar()
print(cardDrew)
