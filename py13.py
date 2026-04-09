import pandas as pd
employee_details = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})
employee_salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
})
sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North', 'North', 'North', 'North', 'North'],
    'Sales': [250, 300, 200, 400, 350]
})
sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South', 'South', 'South', 'South', 'South'],
    'Sales': [300, 320, 280, 360, 310]
})
print("Employee Details:\n", employee_details)
print("\nEmployee Salaries:\n", employee_salaries)
print("\nSales Region 1:\n", sales_region_1)
print("\nSales Region 2:\n", sales_region_2)

merged = pd.merge(employee_details, employee_salaries, on='EmployeeID')

avg_salary = merged.groupby('Department')['Salary'].mean()

print("\nAverage Salary per Department:\n", avg_salary)

merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID', how='inner')

print("\nMerged Employee Data:\n", merged_data)
sales_region_1.set_index('Date', inplace=True)
sales_region_2.set_index('Date', inplace=True)

joined_data = sales_region_1.join(sales_region_2, lsuffix='_North', rsuffix='_South')

print("\nJoined Sales Data:\n", joined_data)

consolidated_sales = pd.concat([sales_region_1, sales_region_2], axis=0)

print("\nConsolidated Sales Data:\n", consolidated_sales)
