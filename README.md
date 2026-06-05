# day2-data-processing
day2 data processing 

Task 1) installing numpy pandas matplotlib

Task 2)Numpy array operations.

Task 3)Employee salary Analysis.

Task 4)Pandas Basics.

Task 5)Employee Details Analysis.

Task 6)CSV processing.

Task 7) Data Cleaning.

Task 8) visualization.

Mini Employee Analytics Dashboard.

Documentation:

# NumPy, Pandas & Employee Analytics Project Documentation

## Project Overview

This project demonstrates the fundamentals of NumPy, Pandas, Data Analysis, Data Cleaning, CSV Processing, Data Visualization, and Dashboard Development. It is designed to build a strong foundation for Data Analytics, Artificial Intelligence (AI), and Machine Learning (ML).

---

# Task 1: Environment Setup

## Objective

Set up a Python development environment and install required libraries.

## Steps

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Required Libraries

```bash
pip install numpy pandas matplotlib
```

### Verify Installation

```python
import numpy
import pandas
import matplotlib

print(numpy.__version__)
print(pandas.__version__)
print(matplotlib.__version__)
```

## Concepts Covered

* Virtual Environments
* Package Management
* Dependency Installation
* Python Libraries

---

# Task 2: NumPy Fundamentals

## Objective

Learn array creation and mathematical operations using NumPy.

## Activities

### Array Creation

* 1D Arrays
* 2D Arrays
* 3D Arrays

### Array Operations

* Addition
* Subtraction
* Multiplication
* Division

### Statistical Operations

* Mean
* Median
* Standard Deviation
* Maximum
* Minimum
* Sum

## Concepts Covered

* ndarray
* Vectorization
* Broadcasting
* Statistical Analysis
* Numerical Computing

## Output

Efficient mathematical calculations using NumPy arrays.

---

# Task 3: Employee Salary Dataset Using NumPy

## Objective

Analyze employee salary data using NumPy.

## Dataset

```python
employee_salaries = [
    25000,
    30000,
    45000,
    55000,
    70000,
    85000,
    100000
]
```

## Analysis Performed

### Average Salary

Calculate mean salary.

### Highest Salary

Find maximum salary.

### Lowest Salary

Find minimum salary.

### Employees Earning Above Average

Filter salaries greater than average salary.

## Concepts Covered

* Statistical Analysis
* Conditional Filtering
* Business Data Analysis

## Output

Salary report displaying key employee salary metrics.

---

# Task 4: Pandas Fundamentals

## Objective

Learn DataFrame creation and manipulation using Pandas.

## Dataset

```python
employees = {
    "id":[1,2,3,4,5],
    "name":["Ajay","Rahul","Priya","Kiran","Sneha"],
    "department":["AI","HR","AI","Finance","HR"],
    "salary":[50000,40000,55000,45000,42000]
}
```

## Operations Performed

### Display DataFrame

View complete dataset.

### Show First Records

```python
df.head(3)
```

### Show Last Records

```python
df.tail(2)
```

### Display Column Names

```python
df.columns
```

### Display Salary Column

```python
df["salary"]
```

### Filter Salary > 45000

```python
df[df["salary"] > 45000]
```

### Filter Department = AI

```python
df[df["department"] == "AI"]
```

## Concepts Covered

* DataFrame
* Series
* Filtering
* Data Selection
* Indexing

---

# Task 5: Employee Analysis

## Objective

Perform employee analytics using Pandas.

## Analysis Performed

### Total Employees

Count employee records.

### Average Salary

Calculate mean salary.

### Highest Salary

Find maximum salary.

### Lowest Salary

Find minimum salary.

### Department-wise Employee Count

Group employees by department.

### Department-wise Average Salary

Calculate average salary for each department.

## Concepts Covered

* GroupBy
* Aggregation
* Business Analytics
* Statistical Reporting

## Output

Department-wise employee insights.

---

# Task 6: CSV Processing

## Objective

Work with CSV files using Pandas.

## Activities

### Create employees.csv

Store at least 20 employee records.

### Read CSV File

```python
pd.read_csv()
```

### Display Data

View employee records.

### Filter Employees

Apply salary-based filtering.

### Sort by Salary

```python
sort_values()
```

### Export Filtered Data

```python
to_csv()
```

## Output File

```text
high_salary_employees.csv
```

## Concepts Covered

* CSV Handling
* File Operations
* Data Export
* Data Filtering

---

# Task 7: Data Cleaning

## Objective

Prepare data for analytics and machine learning.

## Dataset Requirements

Include:

* Missing Names
* Missing Salaries
* Duplicate Records

## Cleaning Operations

### Detect Null Values

```python
isnull()
```

### Remove Duplicates

```python
drop_duplicates()
```

### Fill Missing Values

```python
fillna()
```

### Save Clean Dataset

```python
to_csv()
```

## Output File

```text
cleaned_employees.csv
```

## Concepts Covered

* Missing Data Handling
* Duplicate Removal
* Data Preprocessing
* Data Quality Improvement

---

# Task 8: Data Visualization

## Objective

Visualize employee information using Matplotlib.

## Charts Generated

### Chart 1

Salary Distribution

File:

```text
salary_distribution.png
```

### Chart 2

Department Employee Count

File:

```text
department_employee_count.png
```

### Chart 3

Average Salary by Department

File:

```text
average_salary_by_department.png
```

## Concepts Covered

* Histograms
* Bar Charts
* Data Visualization
* Exploratory Data Analysis (EDA)

---

# Bonus Challenge: Employee Analytics Dashboard

## Objective

Build a menu-driven analytics dashboard.

## Features

### 1. View Employees

Display employee dataset.

### 2. Average Salary

Calculate average employee salary.

### 3. Highest Salary

Display employee with highest salary.

### 4. Department Analysis

Display department-wise statistics.

### 5. Export Report

Generate analytics report.

## Technologies Used

* NumPy
* Pandas

## Output

```text
employee_report.csv
```

## Concepts Covered

* Dashboard Development
* Report Generation
* Menu Driven Programs
* Data Analytics Workflow

---

# Skills Gained

By completing this project, the following skills are developed:

## Python

* Variables
* Lists
* Functions
* File Handling

## NumPy

* Arrays
* Vectorization
* Broadcasting
* Statistics

## Pandas

* DataFrames
* Filtering
* Grouping
* Aggregation

## Data Cleaning

* Missing Values
* Duplicate Handling
* Data Preprocessing

## Data Analysis

* Statistical Analysis
* Business Insights
* Reporting

## Data Visualization

* Histograms
* Bar Charts
* Exploratory Data Analysis

## AI/ML Foundations

* Data Collection
* Data Cleaning
* Feature Engineering
* Data Preprocessing
* Exploratory Data Analysis
* Dataset Preparation

---

# Conclusion

This project provides a complete introduction to NumPy, Pandas, Data Cleaning, Data Analysis, CSV Processing, Visualization, and Dashboard Development. These skills form the foundation required for Data Analyst, AI Engineer, Machine Learning Engineer, and Data Scientist roles.
