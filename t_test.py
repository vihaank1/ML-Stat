import scipy.stats as st
import numpy as np

# -----------------------------
# PART 1: One-sample t-distribution example
# -----------------------------

# Find  critical t-value for a two-tailed test, alpha = 0.05
# Degrees of freedom = 38
t_table = st.t.ppf(1-0.025, 38)
print(t_table)
print("")

# Calculate t
# Formula: (mean1 - mean2) / sqrt( (var1/n1) + (var2/n2) )
t_calc = (80-75)/(np.sqrt((25/20)+(36/20)))
print(t_calc)



# -----------------------------
# PART 2: Another critical t-value example
# -----------------------------

# Here, degrees of freedom = 19, alpha = 0.05 (two-tailed → 0.025 each tail)
ttab_v = st.t.ppf(1-0.025, 19)
print(ttab_v)
print("")


# -----------------------------
# PART 3: Independent sample t-test (manual calculation)
# -----------------------------

Before = np.array([50, 60, 45, 65, 55, 70, 40, 75, 80, 65,
                   70, 60, 50, 55, 45, 75, 60, 0, 65, 70])

After = np.array([60, 70, 55, 75, 65, 80, 50, 85, 90, 70,
                  75, 65, 55, 60, 50, 80, 65, 55, 70, 75])

std_A = np.std(Before)
std_B = np.std(After)

mean_A = np.mean(Before)
mean_B = np.mean(After)

# t-statistic calculation for independent samples
# Formula: (mean_A - mean_B) / sqrt( (std_A^2 / nA) + (std_B^2 / nB) )
t_calc2 = (mean_A-mean_B) / (np.sqrt(((std_A*std_A)/len(Before))+((std_B*std_B)/len(After))))
print(t_calc2)


# -----------------------------
# PART 4: Paired sample t-test 
# -----------------------------

# st.ttest_rel is used when the same subjects are measured twice
# (before and after a treatment → differences are correlated)
t_statistic, p_value = st.ttest_rel(Before, After)

print(t_statistic, "and", p_value)
