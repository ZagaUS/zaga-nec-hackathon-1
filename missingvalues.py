data = [
    {"age": None, "salary": 50000},
    {"age": 30, "salary": None}
]
res=[]
for r in data:
    if r["age"] is None:
      res= r["age"]=1
    if r["salary"]is None:
       res= r["salary"]=1
print("{'age':",res,",""'salary':",res,"}")
