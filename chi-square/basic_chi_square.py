import numpy as np

# Observed vs. expected results of rolling a fair 6-sided die 120 times.
# Null hypothesis (H₀): The die is fair → each side has an equal chance (1/6).
# Significance level: 5%

# Observed frequencies from the actual experiment
observ = np.array([22,17,20,26,22,13])

# Expected frequencies if the die were perfectly fair (120 rolls / 6 sides)
expect = np.array([20,20,20,20,20,20])

# Chi-square Formula: χ² = Σ((Observed - Expected)² / Expected)
chi_square = np.sum(np.square(observ-expect)/expect)

print(chi_square) # Print chi-square value where α = 0.05

# Interpretation:
# If χ² ≤ critical value → fail to reject H₀ → die is fair.
# If χ² >  critical value → reject H₀ → die is biased.

