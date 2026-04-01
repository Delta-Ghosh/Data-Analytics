name= input("What is your name? ")
age = int(input("What is your age? "))
print(name + " is " + str(age) + " years old.") # This is the old way of doing it. It is a bit clumsy and not very efficient.
print(f"{name} is {age} years old.")