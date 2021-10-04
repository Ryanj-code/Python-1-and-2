#Ryan, Briana

#Shipping Cost
weight = float(input("what is the weight of the package in pounds?"))
if weight <= 2:
  newWeight = weight * 1.50
  print("you pay $ " + str(newWeight))
elif weight >2 and  weight <=6:
  newWeight = weight * 3 
  print("you pay $ " + str(newWeight))
elif weight >6 and weight <=10:
  newWeight = weight * 4  
  print("you pay $ " + str(newWeight))
else:
  newWeight = weight * 4.75  
  print("you pay $ " + str(newWeight))
 
#Cookies Recipe
amount = int(input("How many cookies?"))
number = 48
fraction = float(amount / number)
sugar = (1.5 * fraction)
butter = (1 * fraction)
flour = (2.75 * fraction)
print("You need " + str(sugar) + " cups of sugar")
print("You need " + str(butter) + " cups of butter")
print("You need " + str(flour) + " cups of flour") 
