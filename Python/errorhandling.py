print ("initialing")

a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
try:
    print ("The Value of a/b is :", a/b)
except ZeroDivisionError:
    print("ZeroDivisionError")
    
print ("Done")