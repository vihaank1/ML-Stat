import scipy.stats as st
import numpy as np


# -------------------------------
# Example 1: Z-test for a single sample mean
# -------------------------------

S_x = 90
P_u = 82
P_std = 20
n = 81
al = 0.05     # Significance level (alpha)

# Calculate the Z statistic
# Formula: Z = (sample mean - population mean) / (population std / sqrt(sample size))
z_calc = (S_x - P_u)/(P_std/np.sqrt(n))
print(z_calc)

# Find Z critical val
z_table = st.norm.ppf(1-al)
print(z_table)
print("")

# Decision rule: If Z_calculated > Z_critical → reject H₀ (accept H₁)
if z_table < z_calc:
    print("ha is right")
else:
    print("ho is right")

print("")

# -------------------------------
# Example 2: Z-test for the difference between two sample means
# -------------------------------

# Old design conversion times
old_design_data = np.array([45.2, 42.8, 38.9, 43.5, 41.0, 44.6, 40.5, 42.7,
                            39.8, 41.4, 44.3, 39.7, 42.1, 40.6, 43.0, 42.2, 41.5, 39.6, 44.0, 43.1, 38.7,
                            43.9, 42.0, 41.9, 42.8, 43.7, 41.3, 40.9, 42.5, 41.6])
# New design conversion times 
new_design_data = np.array(
    [48.5, 49.1, 50.2, 47.8, 48.7, 49.9, 48.0, 50.5, 49.8, 49.6,
     48.2, 48.9, 49.7, 50.3, 49.4, 50.1, 48.6, 48.3, 49.0, 50.0,
     48.4, 49.3, 49.5, 48.8, 50.6, 50.4, 48.1, 49.2, 50.7, 50.8])


tot_std = 2.5                   # standard deviation for both groups
n_sp= len(new_design_data)      # Sample size for both groups
aPl = 0.05                      # Significance level (alpha)

# means of both samples
mean_old=np.mean(old_design_data)
mean_new=np.mean(new_design_data)

# Find Z statistic for two means
z_find = (mean_new-mean_old)/(tot_std/np.sqrt(n_sp))
print(z_find)

# Critical Z val for one-tailed test
z_discover = st.norm.ppf(1-aPl)
print(z_discover)
print("")

# Decision rule: If Z_calculated > Z_critical → reject H₀
if z_calc > z_table:
    print("ha is actually right!!")
else:
    print("hmmmm, ho is right")
