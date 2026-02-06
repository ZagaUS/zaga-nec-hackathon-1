
import pandas as pd
#from sklearn.model_selection import test_train_split


data = [
    {"height": 150, "weight": 50},
    {"height": 160, "weight": 60},
    {"height": 170, "weight": 80}
]

df = pd.DataFrame(data)
x = df[["height", "weight"]]
x_std = (x-x.min())/(x.max()-x.min()) #Instaed of Min_Mx scaling i have used formula
x_scaled = x_std*(1-0)+0
sc_data = x_scaled.values
scaled_df = pd.DataFrame(sc_data, columns=["height", "weight"])
print(scaled_df)