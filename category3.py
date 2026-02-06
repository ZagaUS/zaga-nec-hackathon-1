data = [
    {"customer_id": 101, "churn": 1},
    {"customer_id": 102, "churn": 0},
    {"customer_id": 103, "churn": 1},
    {"customer_id": 104, "churn": 0},
    {"customer_id": 105, "churn": 1}
]
churn_count = {}
for record in data:
    churn = record['churn']
    churn_count[churn] = churn_count.get(churn, 0) + 1
print(churn_count)