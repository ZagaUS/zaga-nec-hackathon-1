data = [
    {"salary": 40000},
    {"salary": 50000},
    {"salary": 60000}
]

mean=sum(d["salary"] for d in data)/len(data)
std_dev=(sum((d["salary"]-mean)**2 for d in data)/len(data))**0.5
for d in data:
    d["z_score"]=(d["salary"]-mean)/std_dev
print(data)

