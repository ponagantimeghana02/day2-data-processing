import pandas as pd
import numpy as np


df = pd.read_csv("employees.csv")

while True:
    print("\n===== Employee Analytics Dashboard =====")
    print("1. View Employees")
    print("2. Average Salary")
    print("3. Highest Salary")
    print("4. Department Analysis")
    print("5. Export Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEmployee Data:")
        print(df)

    elif choice == "2":
        avg_salary = np.mean(df["Salary"])
        print(f"\nAverage Salary: {avg_salary:.2f}")

    elif choice == "3":
        highest_salary = df["Salary"].max()
        employee = df[df["Salary"] == highest_salary]

        print("\nEmployee(s) with Highest Salary:")
        print(employee)

    elif choice == "4":
        print("\nDepartment Analysis:")
        dept_analysis = df.groupby("Department")["Salary"].agg(
            Employee_Count="count",
            Average_Salary="mean",
            Maximum_Salary="max",
            Minimum_Salary="min"
        )
        print(dept_analysis)

    elif choice == "5":
        report = pd.DataFrame({
            "Metric": [
                "Total Employees",
                "Average Salary",
                "Highest Salary",
                "Lowest Salary"
            ],
            "Value": [
                len(df),
                df["Salary"].mean(),
                df["Salary"].max(),
                df["Salary"].min()
            ]
        })

        report.to_csv("employee_report.csv", index=False)
        print("\nReport exported successfully as employee_report.csv")

    elif choice == "6":
        print("Exiting Dashboard...")
        break

    else:
        print("Invalid choice! Please try again.")