import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.describe())
print("")

print(np.percentile(df["age"].dropna(),25), np.percentile(df["age"].dropna(),75))

print(df["age"].skew())
print(" ")

dat = np.random.normal(0,100,100)

greenery=pd.DataFrame({"x": dat})

print(greenery["x"].skew())


sns.histplot(x="age", data=df)
plt.show()

