import numpy as np

# Observed vs expected 6 side dice rolls for 120 rolls, 5% level of significance
observ = np.array([22,17,20,26,22,13])
expect = np.array([20,20,20,20,20,20])

# ultimately dice is fair due to ho
chi_square = np.sum(np.square(observ-expect)/expect)
print(chi_square)


