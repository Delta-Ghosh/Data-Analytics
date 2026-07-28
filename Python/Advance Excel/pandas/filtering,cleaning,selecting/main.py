import pandas as pd

df = pd.DataFrame({
    "Product Name": [" iPhone 14 ", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] * 200,
    "price": ["499", "799", "1199", "899", None] * 200,
    "category": ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes ", " no", None] * 200,
    "launch_year": ["2023", "2022", "2021", "2020", None] * 200
})

# df = df.rename(columns={"Product Name": "product_name"}) # descriptive statistics
# print (df[['product_name', 'price' , 'in_stock']]) # display specific columns
# print(df[df['in_stock']== "Yes"]) # display rows where 'in_stock' is "Yes"
# print(df[(df['reviews'] > 500) & (df['in_stock']== "Yes")]) # display rows where 'reviews' is greater than 500 and 'in_stock' is "Yes"
# print(df.isna().sum()) # display the number of missing values in each column
# df["rating"] = df["rating"].fillna(df["rating"].mean()) # fill missing values in 'rating' column with the mean of the column
# df["price"] = df["price"].astype(float) # convert 'price' column to float data type
# df["category"] = df["category"].str.lower().str.strip() # convert 'category' column to lowercase and remove leading/trailing spaces
# print(df.head()) # display the first 5 rows of the DataFrame