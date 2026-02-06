import pandas as pd 

data = [
    {"score": 85},
    {"score": None},
    {"score": 90},
    {"score": 75}
]
df=pd.DataFrame(data)
variable = df['score'].isnull()

print(variable)