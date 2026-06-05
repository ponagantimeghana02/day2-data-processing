#Task 3:

# Employee Salary Analysis

employee_salaries = [
    25000,
    30000,
    45000,
    55000,
    70000,
    85000,
    100000
]
average_salary = sum(employee_salaries) / len(employee_salaries)
highest_salary = max(employee_salaries)
lowest_salary = min(employee_salaries)
above_average=[]
for salary in employee_salaries:
    if salary>average_salary:
        above_average.append(salary)


print("Employee Salary Report: ")
print(f"Average Salary: ₹{average_salary:.2f}")
print(f"Highest Salary: ₹{highest_salary}")
print(f"Lowest Salary: ₹{lowest_salary}")
print(f"Employees Earning Above Average: {len(above_average)}")
print("Salaries Above Average:", above_average)