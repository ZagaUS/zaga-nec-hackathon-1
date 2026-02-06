data=["ml","ai","ml","ai","ds","ml"]
frequency={}
for item in data:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)
