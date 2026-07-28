import pandas as pd

data = {
    "name": ["Ali", "Sara", "John" , "Sarthak" , "Soumili" , "Rohit" , "Virat"],
    "marks": [85, 90, 78, 90 , 95, 88, 92]
}

df = pd.DataFrame(data)
print(df)
print(df.describe()) # describe the data
print(df.info()) # describe the data types and non-null values
print(df.head()) # display the first 5 rows of the DataFrame
print(df.tail()) # display the last 5 rows of the DataFrame
print(df['name']) # display the 'name' column
print(df['marks']) # display the 'marks' column
print(df[['name', 'marks']]) # display both 'name' and 'marks' columns
print(df.shape) # display the shape of the DataFrame