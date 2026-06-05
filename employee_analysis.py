import pandas as pd

# Employee Data
employees = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ajay", "Rahul", "Priya", "Kiran", "Sneha"],
    "department": ["AI", "HR", "AI", "Finance", "HR"],
    "salary": [50000, 40000, 55000, 45000, 42000]
}

# Create DataFrame
df = pd.DataFrame(employees)

# Analysis
total_employees = len(df)
average_salary = df["salary"].mean()
highest_salary = df["salary"].max()
lowest_salary = df["salary"].min()

dept_employee_count = df.groupby("department")["id"].count()
dept_average_salary = df.groupby("department")["salary"].mean()

# Output Report
print("Employee Analysis Report")

print(f"Total Employees:\n {total_employees}")
print(f"Average Salary:\n ₹{average_salary:.2f}")
print(f"Highest Salary:\n ₹{highest_salary}")
print(f"Lowest Salary:\n ₹{lowest_salary}")

print("\nDepartment-wise Employee Count:")
print(dept_employee_count)

print("\nDepartment-wise Average Salary:")
print(dept_average_salary)