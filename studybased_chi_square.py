import numpy as np

# Observed frequencies: [Pop, Hip hop, Classical, Rock]
# Row1 = Male counts, Row2 = Female counts
row1 = np.array([40,45,25,10])
row2 = np.array([35,30,20,30])

sum_r1 = np.sum(row1)
sum_r2 = np.sum(row2)

# Row totals (sum of each gender's preferences)
sum_row = np.array([sum_r1, sum_r2])
print(sum_row)
print("")

# Column totals (sum of each genre's preferences across genders)
sum_column = row1 + row2
print(sum_column)
print("")

# Expected frequencies under H₀ (no association between gender & genre)
exp = []
for i in sum_row:
    for j in sum_column:
        value = (i*j)/235    # Formula: (row total × column total) / total sample
        exp.append(value)
        

obj = np.array([40,45,25,10,35,30,20,30])

# Chi-square statistic: Σ((O - E)² / E)
chi_square = np.sum(np.square((obj-exp))/exp)
print("chi square calc:", chi_square)


# Problem summary:
# Test at 5% significance level if gender is associated with music preference.
# If χ² > χ² critical value → reject H₀ → significant association exists.
# Conclusion in this case: Ha is true → gender and music preference are related.
