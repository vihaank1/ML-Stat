import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a population of 10,000 random integers between 10 and 100
pop = [np.random.randint(10,100) for i in range(10000)]
pop_table = pd.DataFrame({"Pop data": pop})
print(np.mean(pop))   # Print actual population mean

sns.kdeplot(x="Pop data", data=pop_table)
plt.show()


sample_mean=[]
for num_sample in range(65):
    sample_data=[]
    for data in range(500):
        sample_data.append(np.random.choice(pop))
    sample_mean.append(np.mean(sample_data))

# Print mean of all sample means (should be close to the population mean)
print(np.mean(sample_mean))
sample_M=pd.DataFrame({"Sample_Mean": sample_mean})     # Convert the sample means into a DataFrame

sns.kdeplot(x="Sample_Mean", data=sample_M)
plt.show()
