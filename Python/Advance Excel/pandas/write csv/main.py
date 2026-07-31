import pandas as pd

#sample data of e commerce products
df = pd.DataFrame({
    "Product Name": [" iPhone 14 ", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] ,
    "price": ["499", "799", "1199", "899", None] ,
    "category": ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] ,
    "rating": [5, 4, None, 3, 2] ,
    "reviews": [1200, 3400, 560, 780, 150] ,
    "in_stock": ["Yes", "No", "yes ", " no", None] ,
    "launch_year": ["202    3", "2022", "2021", "2020", None] })

print(df)

#create a dataframe for products
df2 = pd.DataFrame({
    "Product Name": ["iPhone 14", "Samsung Galaxy", "OnePlus 11", "Pixel 7", "Nokia 3310"] ,
    "price": ["499", "799", "1199", "899", "59"] ,
    "category": ["Mobile", "Mobile", "Electronics", "Electronics", "Mobile"] ,   
    "rating": [5, 4, 4, 3, None],
    "reviews": [1200, 3400, 560, 780, 10],
    "in_stock": ["Yes", "No", "Yes", "No", "Yes"],
    "launch_year": ["2023", "2022", "2021", "2020", "2000"]
})

print(df2)

# with pd.ExcelWriter("report.xlsx") as writer: # create an Excel writer object
#     df.to_excel(writer, sheet_name="Sales", index=False) # write the first DataFrame to an Excel file
#     df2.to_excel(writer, sheet_name="Users", index=False) # write the second DataFrame to a different sheet in the same Excel file

df[["Product Name", "price", "category"]].to_csv("products.csv", index=False) # write the selected columns to a CSV file