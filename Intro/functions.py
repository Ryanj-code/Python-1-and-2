import math
#Hypotenuse function
def hypotenuse(number):
  print(math.sqrt(number))

sideA = int(input("Give me a number for a leg: "))
sideB = int(input("Give me another number for another leg: "))
totalSide = (sideA**2) + (sideB**2)
number = totalSide 
hypotenuse(number)

#Rock Paper and Scissors function
def rockPaperScissors(user, computer):
  if user == "rock" and computer == "paper":
    print("Lose")
  elif user == "rock" and computer == "rock":
    print("Tie")
  elif user == "rock" and computer == "scissors":
    print("Win")
  
  if user == "paper" and computer == "rock":
    print("Win")
  elif user == "paper" and computer == "paper":
    print("Tie")
  elif user == "paper" and computer == "scissors":
    print("Lose")
  
  if user == "scissors" and computer == "paper":
    print("Win")
  elif user == "scissors" and computer == "scissors":
    print("Tie")
  elif user == "scissors" and computer == "rock":
    print("Lose")

user = str(input("User: "))
com = str(input("Computer: "))
rockPaperScissors(user, com)
