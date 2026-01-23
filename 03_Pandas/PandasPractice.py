import pandas as pd
#Series
ser = [1, 2, 3, 4, 5]
ser = pd.Series(ser,index=['a','s','d','f','g'],name="Numbers",dtype="float64")

s1 = pd.Series(10,index=[1,2,3,4,5,6] )
s2 = pd.Series(11,index=[1,2,3,4] )
print (s1+s2)

#DataFrame
data = {
    "Name": ["Simran", "singh", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
res = pd.DataFrame(data,columns=["Name","Age"])
print(res)

data2 = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
}
#Creating new columns based on operations
res2 = pd.DataFrame(data2)
res2["C"] = res2["A"] + res2["B"]
res2["D"] = res2["A"] * res2["B"]
res2["E"] = res2["D"] - res2["C"]
res2["Bool"] = res2["E"] > 10
print(res2)

#Insert and Delete Data

res2.insert(2,"Python",[11,12,12])
print(res2)

res2.pop("Python")
print(res2.pop("Bool"))
print(res2)

#Creating and Reading of CSV files
data3 = {
    "Product": ["Laptop", "Smartphone", "Tablet"],
    "Price": [1000, 500, 300],
    "Stock": [50, 200, 150]
}

#This creates two csv files with different headers
res3 = pd.DataFrame(data3)
res3.to_csv("products.csv",index=False)
res3.to_csv("products_2.csv",index=False,header = ["Product_Name","Product_Price","Product_Stock"])

#Reading CSV files
df = pd.read_csv("products.csv")
print(df)

#Reading specific number of rows from CSV
df2 = pd.read_csv("products_2.csv",nrows=2)
print(df2)

#Selecting specific columns while reading CSV
csv_data = pd.read_csv("products_2.csv",usecols=["Product_Price","Product_Stock"])
print(csv_data)

#Reading CSV with index column
csv_data2 = pd.read_csv("products_2.csv",index_col="Product_Name")
print(csv_data2)

#Reading CSV with custom header row
csv_data3 = pd.read_csv("products_2.csv",header=2)
print(csv_data3)

#PANDAS FUNCTIONS

print (csv_data.columns) # Get column names

print (csv_data.index)   # Get row indices

print (csv_data.describe()) # Get summary statistics


print (csv_data.info()) # Get info about DataFrame

cancer_data = pd.read_csv("cancer-risk-factors.csv")
print(cancer_data.head())  # Display first 5 rows