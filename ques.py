import pandas as pd 


a = [10, 20, 30, 40, 50, 20]
b = [30, 60, 20, 70]

variable = pd.Series(a).drop_duplicates().isin(b)

islist= variable.tolist()
print(variable)
