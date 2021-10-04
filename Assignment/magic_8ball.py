import random

def magicEight(user_name):
  results = ['outlook is good','ask again later','yes','no','most likely no','most likely yes','maybe','outlook is not good']
  randomChoice = random.randint(0,len(results) - 1)
  print(user_name + ", " + results[randomChoice])
user_name = input("What is your name?")
user_ques = input("What is your question?")
magicEight(user_name)
