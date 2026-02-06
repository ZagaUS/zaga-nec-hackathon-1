import pandas as pd
data = [
    {"exp_years": 2, "edu_level": 1},
    {"exp_years": 5, "edu_level": 2},
    {"exp_years": 10, "edu_level": 3}
]
df=pd.DataFrame(data)
df['exp_edu']=df['exp_years']*df['edu_level']
print(df['exp_edu'])
