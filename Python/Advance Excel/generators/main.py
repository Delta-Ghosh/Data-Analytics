def complex_cal(i):
    #some complex calculation
    return i

def get_numbers():
    for i in range(5):
        yield complex_cal(i)

a= get_numbers()
print(next(a))
print(next(a))
print(next(a))
