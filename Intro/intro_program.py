#declare variable
student_name = input("What's your name?")
#user input
favorite_subject = int(input("What's your favorite_subject? Type 1 for art/music, 2 for math, 3 for English, 4 for science, 5 for phys ed, or 6 for history."))
#if, else if, and else statements
if favorite_subject > 0 and favorite_subject < 7:
  if favorite_subject == 1 :
    print(student_name + ", did you know Pixar started out as a computer graphics studio? computers can make art and music larger than life!")
  elif favorite_subject == 2:
       print(student_name + ",that's awesome! Mathematicians write computer programs to run simulations so they can experiment and test models")
  elif favorite_subject == 3:
       print(student_name = ",that's great! Computer programmers plan and pay attention to syntax just like when you write essays")
  elif favorite_subject == 4:
       print("The Apollo computers that sent us to the moon were no more powerful than a pocket calculator today. Imagine that, " + student_name + "!")    
  elif favorite_subject == 5:
       print("Guess what" + student_name + "? With computer science, you can learn to code your own fitness tracker app!")  
  else:
       print(student_name + ", did you know that computer scientist Alan Turing helped the Alliance win WWII by craking coded Nazi messages?")
else:print("Invalid respones.")
