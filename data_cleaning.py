import pandas as pd

df = pd.read_csv("employees.csv")

print("Original Dataset\n")
print(df)

print("Null Values \n")
print(df.isnull().sum())

df = df.drop_duplicates()

df["name"] = df["name"].fillna("Unknown")

avg_salary = df["Salary"].mean()
df["salary"] = df["Salary"].fillna(avg_salary)

df.to_csv("cleaned_employees.csv", index=False)

print("Cleaned Dataset\n")
print(df)

print("\nDataset saved as 'cleaned_employees.csv'")