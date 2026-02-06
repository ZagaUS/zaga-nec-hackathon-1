data = [{'date': '2023-07-15'}]

for item in data:
    date_str = item['date']
    parts = date_str.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    item['date'] = date_str 
    item['year_month'] = f"{year:04d}-{month:02d}"

print("date year_month")
for i, item in enumerate(data):
    print(f"{i} {item['date']}   {item['year_month']}")
