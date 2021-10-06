#Fizzbuzz code
max = int(input("Maximum number: "))
for number in range(1, max + 1):
  if number % 5 == 0 and number % 3 == 0:
    print("FIZZBUZZ")
  elif number % 3 == 0:
    print("FIZZ")
  elif number % 5 == 0:
    print("BUZZ")
  else:
    print(number)
#Prints fizz is the number is divisible by 3, buzz if divisible by 5, fizzbuzz is divisible by 3 & 5, else prints the number.
