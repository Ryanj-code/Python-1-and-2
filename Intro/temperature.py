T = int(input("Give me a number"))
answer = int(input("Choose 1 to convert from farenheit to celsius, Choose 2 to convert from celsius to farenheit"))

farenheit = (T * 1.8 + 32)
farenheit = round(farenheit, 1)
celsius = (T - 32) / 1.8
celsius = round(celsius, 1)

if answer == 1: 
  print("The celsius is " + str(celsius))
else:
  print("The farenheit is " + str(farenheit))
