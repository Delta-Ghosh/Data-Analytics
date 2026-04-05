a = "Sarthak. good morning"

# file = open("Sarthak.txt", "w") # w for write, if the file does not exist it will create a new file, if the file already exists it will overwrite the existing content
# file.write(a) # file.close() # close the file after writing to it

file = open("Sarthak.txt", "r") # r for read
content = file.read() # read the content of the file and store it in a variable
print(content)


file.close()