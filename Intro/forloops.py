#Adds all numbers from 1 to n and prints results.
value = int(input("Input a number you want to stop at."))
sum = 0
for number in range(1 , value + 1):
  sum += number
print("The numbers from 1 to " + str(value) + " add up to " + str(sum))

#Adds all numbers not divisible by 3 and 5, then prints result.
userNumber = int(input("Maximum number: "))
sum = 0
for i in range(1 , userNumber + 1):
  if not(i % 3 == 0 or i % 5 == 0):
    sum += i 
print(sum)
