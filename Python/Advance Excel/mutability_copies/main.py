a = [2,4,5,10]

b = a  # value of a is assigned to b, both a and b point to the same list object
b= a.copy() #copy of a


b[1]=20    
print(a)