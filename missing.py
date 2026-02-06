data = [
    {"age": 25, "gender": "Male", "salary": 50000},
    {"age": None, "gender": "Female", "salary": 60000},
    {"age": 30, "gender": "Male", "salary": None},
    {"age": 22, "gender": "Female", "salary": 45000}
]
for record in data:
    if record ["gender"]=="Male":
        record["gender"]=1
    else:
        record["gender"]=0
    if record["age"] is None:
        record["age"]=0
    if record["salary"] is None:
        record["salary"]=0
print(data)
