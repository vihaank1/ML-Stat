
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

group_a=np.array([75,65,73,68,72,76])
group_b=np.array([90,47,43,96,93,51])

# We find the standard deviation of both groups
print(np.std(group_a), np.std(group_b))
print("")
# We find variances
print(np.var(group_a), np.var(group_b))


