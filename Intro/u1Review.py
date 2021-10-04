#Problems for Unit 1 Review
#Walking problem 1
print("My name is Ryan.")
print("My dream job is to be a programmer.")
print("Next week I will be staying home and playing video games.\n")

#walking problem 2
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hi " + first_name + " " + last_name + ".\n")

#jogging problem 1 
message = ("I Have a Dream.")
famous_person = ("Luther King Jr")
print(famous_person + ": " + message + "\n")

#jogging problem 2
number = int(input("Give me a number: "))
if number % 2 == 0:
  print("The number is even.\n")
elif number % 2 == 1:
  print("The number is odd.\n") 

#running problem 1 
user_radius = int(input("Radius of Circle: "))
import math
print("Area: ")
print((user_radius ** 2) * math.pi)
print("\n")

#running problem 2
user_seconds = int(input("Number of seconds: "))
minutes = int(user_seconds / 60)
seconds = int(user_seconds % 60)
hours = int(user_seconds / 3600)
print(str(user_seconds) + " seconds is equal to " + str(hours) + " hours " + str((minutes) % 60) + " minutes and " + str(seconds) + " seconds")
