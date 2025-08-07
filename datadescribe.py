import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

# Print summary statistics 
print(df.describe())
print("")

# Print the 25th percentile and 75th percentile of the "age" column
# dropna() removes missing (NaN) values so calculation doesn't break
print(np.percentile(df["age"].dropna(),25), np.percentile(df["age"].dropna(),75))

# Print skewness of the "age" column
print(df["age"].skew())
print(" ")

# Generate 100 random values from a normal distribution
dat = np.random.normal(0,100,100)

# Put the random data into a new DataFrame column 
greenery=pd.DataFrame({"x": dat})

# Print skewness of the random "x" data
print(greenery["x"].skew())


sns.histplot(x="age", data=df)
plt.show()

