#CSV Processing

import pandas as pd

df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

# Filter employees with salary > 50000
high_salary_df = df[df["Salary"] > 50000]

print("Employees with Salary > 50000 \n")
print(high_salary_df)

sorted_df = df.sort_values(by="Salary", ascending=False)
print("Employees Sorted by Salary\n")
print(sorted_df)

high_salary_df.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered data exported to 'high_salary_employees.csv'")