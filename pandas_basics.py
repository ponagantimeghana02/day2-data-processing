#Task 4:

# Perform:
# Operations
#  Display DataFrame 
#  Show first 3 records 
#  Show last 2 records 
#  Display column names 
#  Display salary column 
#  Filter salary > 45000 
#  Filter department = AI 

import pandas as pd

employees = {
    "id":[1,2,3,4,5],
    "name":["Ajay","Rahul","Priya","Kiran","Sneha"],
    "department":["AI","HR","AI","Finance","HR"],
    "salary":[50000,40000,55000,45000,42000]
}

df=pd.DataFrame(employees)

print("Displaying DataFrame\n",df)
print("First 3 records are:\n",df.head(3))
print("Last 2 records are:\n",df.tail(2))
print("Column names are:\n",df.columns)
print("Displaying salary column are:\n",df[df["salary"]>45000])
print("Employees in AI Department:\n",df[df["department"]=="AI"])