data = [
    {"id": 1, "score": 80},
    {"id": 2, "score": 90},
    {"id": 1, "score": 80}
]
seen = set() 
result = [] 
for d in data:     
    if d['id'] not in seen:         
        result.append(d) 
        seen.add(d['id']) 
print(result) 

