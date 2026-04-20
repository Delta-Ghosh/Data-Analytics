try:
    x = int(input("Enter a number: "))
    y= 10/x
except ValueError:
    print("ValueError: Please enter a valid integer.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
finally:
    print("This block will always execute.")