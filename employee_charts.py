import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")


plt.figure(figsize=(8, 5))
plt.hist(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.close()


dept_count = df["Department"].value_counts()

plt.figure(figsize=(8, 5))
dept_count.plot(kind="bar")
plt.title("Department Employee Count")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("department_employee_count.png")
plt.close()


avg_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("average_salary_by_department.png")
plt.close()

print("Charts saved successfully!")