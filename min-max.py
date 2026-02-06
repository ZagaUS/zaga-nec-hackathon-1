data = [
    {"salary": 40000},
    {"salary": 60000},
    {"salary": 80000}
]
salaries = [item["salary"] for item in data]
min_salary = min(salaries)  
max_salary = max(salaries)
print("Minimum Salary:", min_salary)
print("Maximum Salary:", max_salary)    



