import random

#Print random numbers in the same line.
line = ""
for i in range(5):
   line += str(random.randrange(1,71))
   line += " "
line += str(random.randrange(1,26)) 
print(line)
