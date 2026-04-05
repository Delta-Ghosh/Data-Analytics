# def show_value():
#     x = 10 # Local variable x is defined inside the function
#     print(x)
# show_value()
# x= 20 # Global variable x is defined outside the function
# show_value()

x= 10 # Global variable x is defined outside the function
def show_value():
    x = 20 # Local variable x is defined inside the function
show_value()
print(x) # Accessing the global variable x outside the function