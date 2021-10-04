#asking for the noun and the amount
noun=input("Give me a singular noun")
amount=int(input("How much of that noun?"))
#chained conditions for changing end of the word to plural verison or keep the same
if amount == 1: 
  print("1 " + str(noun))
elif noun[-2:] == "fe":
  print(str(amount) + " " + noun[:-2] + "ves")
elif noun[-1:] == "y":
  print(str(amount) + " " + noun[:-1] + "ies")
elif noun[-2:] == "sh" or noun[-2:] == "ch":
  print(str(amount) + " " + noun + "es")
elif noun[-2:] == "us":
  print(str(amount) + " " + noun[:-2] + "i")
elif noun[-2:] == "ay" or noun[-2:] == "oy" or noun[-2:] == "ey" or noun[-2:] == "uy":
  print(str(amount) + " " + noun[:-2] + "s") 
elif noun[-2:] == "is":
#special cases
  print(str(amount) + " " + noun[:-2] + "es")
elif noun[-1:] == "a":
  print(str(amount) + " " + noun[:-1] + "ae")
elif noun[-4:] == "ouse":
  print(str(amount) + " " + noun[:-4] + "ice")   
  #else we just add s to the noun
else: 
  print(str(amount) + noun + "s")
