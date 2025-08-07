import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load tips dataset from seaborn
df = sns.load_dataset("tips")
print(df.head())
print("")

# Calculate the correlation matrix for numeric columns
correlation = df.select_dtypes(["float64", "int64"]).corr()
print(correlation)
print("")

# Calculate the covariance matrix for numeric columns
covar = df.select_dtypes(["float64", "int64"]).cov()
print(covar)

# Plot correlation matrix as a heatmap
plt.figure(figsize=(4,3))
sns.heatmap(correlation, annot=True) # annot=True adds the values inside each cell
plt.show()

# Plot covariance matrix as a heatmap
plt.figure(figsize=(4,3))
sns.heatmap(covar, annot=True)
plt.show()
