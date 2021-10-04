#Use nested for loops for square.
def square(value): 
  for a in range(value):
    print()
    for i in range(value): 
      print("* ",end = " ")
  print("\n")

square(5)

#Use nested for loops for rectangle.
def rectangle(row, column):
  for r in range(row):
    print()
    for c in range(column):
      print("* ",end = " ")
  print("\n")

rectangle(5,8)

#Use a for loop to make right triangle.
def rightTriangle(number): 
  value = ""
  for a in range(number):
    value += ("* ")
    print(value)
  print("\n")

rightTriangle(5)

#Use nested for loops to make a number triangle that increments each row.
def numTriangle(number):
  x = 0
  line = ""
  for i in range(number):
    value = 0
    x += 1
    for a in range(x):
      value = value + 1
      line += str(value)
    line += "\n"
  print(line)

numTriangle(3)
