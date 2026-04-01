s1 = {"sarthak", "swastik", "soumili"}
s1.add("Ahana")

s1.update(["Sukla"])
print(len(s1)) # This will print the number of unique elements in the set, which is 5.
s1.discard("sarthaka") #discard does not throw error if element is not present in the set
a=s1.pop() # This will remove and return an arbitrary element from the set. If the set is empty, it will raise a KeyError.
print(s1)
print(a)

first={1,5,6,7}
secound={5,6,7,8}
print(first.union(secound)) # This will print the union of the two sets, which is
print(first.intersection(secound)) # This will print the intersection of the two sets, which is {5, 6, 7}.
print(first.difference(secound)) # This will print the difference of the two sets, which is {1}.
print(first.symmetric_difference(secound)) # This will print the symmetric difference of the two sets, which is {1, 8}.
