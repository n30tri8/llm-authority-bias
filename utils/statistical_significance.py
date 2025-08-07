import scipy.stats as stats
import numpy as np

def chi_squared_proportions(prop_a, n_a, prop_b, n_b, alpha=0.05):
    # Convert proportions to counts
    success_a = round(prop_a * n_a)
    failure_a = n_a - success_a

    success_b = round(prop_b * n_b)
    failure_b = n_b - success_b

    # Contingency table
    table = np.array([
        [success_a, failure_a],
        [success_b, failure_b]
    ])

    # Chi-squared test (without Yates' correction, like MedCalc)
    chi2, p, dof, expected = stats.chi2_contingency(table, correction=False)

    return chi2, p

print("Chi-squared test results for Qwen-7b:")
# Qwen-7B
# EN: female (427, 0.611) vs male (427, 0.621)
chi2, p = chi_squared_proportions(0.611, 427, 0.621, 427)
print(chi2, ", ", p)

# AR: female (290, 0.693) vs male (290, 0.755)
chi2, p = chi_squared_proportions(0.693, 290, 0.755, 290)
print(chi2, ", ", p)

# DE: female (381, 0.648) vs male (381, 0.583)
chi2, p = chi_squared_proportions(0.648, 381, 0.583, 381)
print(chi2, ", ", p)

# HI: female (263, 0.707) vs male (263, 0.703)
chi2, p = chi_squared_proportions(0.707, 263, 0.703, 263)
print(chi2, ", ", p)

# IT: female (374, 0.538) vs male (374, 0.487)
chi2, p = chi_squared_proportions(0.538, 374, 0.487, 374)
print(chi2, ", ", p)

# JA: female (344, 0.657) vs male (344, 0.590)
chi2, p = chi_squared_proportions(0.657, 344, 0.590, 344)
print(chi2, ", ", p)


# Llama-7b
print("Chi-squared test results for Llama-7b:")
# Pair 1: female (404, 0.396) vs male (404, 0.273)
chi2, p = chi_squared_proportions(0.396, 404, 0.273, 404)
print(chi2, ", ", p)

# Pair 2: female (288, 0.823) vs male (288, 0.840)
chi2, p = chi_squared_proportions(0.823, 288, 0.840, 288)
print(chi2, ", ", p)

# Pair 3: female (348, 0.405) vs male (348, 0.256)
chi2, p = chi_squared_proportions(0.405, 348, 0.256, 348)
print(chi2, ", ", p)

# Pair 4: female (235, 0.413) vs male (235, 0.281)
chi2, p = chi_squared_proportions(0.413, 235, 0.281, 235)
print(chi2, ", ", p)

# Pair 5: female (350, 0.140) vs male (350, 0.066)
chi2, p = chi_squared_proportions(0.140, 350, 0.066, 350)
print(chi2, ", ", p)

# Pair 6: female (309, 0.521) vs male (309, 0.518)
chi2, p = chi_squared_proportions(0.521, 309, 0.518, 309)
print(chi2, ", ", p)

# Llama-7b
print("Chi-squared debiased test results for Llama-7b:")

# Pair 1: female (404, 0.300) vs male (404, 0.135)
chi2, p = chi_squared_proportions(0.300, 404, 0.135, 404)
print(chi2, ", ", p)

# Pair 2: female (288, 0.740) vs male (288, 0.719)
chi2, p = chi_squared_proportions(0.740, 288, 0.719, 288)
print(chi2, ", ", p)

# Pair 3: female (348, 0.109) vs male (348, 0.078)
chi2, p = chi_squared_proportions(0.109, 348, 0.078, 348)
print(chi2, ", ", p)

# Pair 4: female (235, 0.230) vs male (235, 0.119)
chi2, p = chi_squared_proportions(0.230, 235, 0.119, 235)
print(chi2, ", ", p)

# Pair 5: female (350, 0.023) vs male (350, 0.014)
chi2, p = chi_squared_proportions(0.023, 350, 0.014, 350)
print(chi2, ", ", p)

# Pair 6: female (309, 0.382) vs male (309, 0.311)
chi2, p = chi_squared_proportions(0.382, 309, 0.311, 309)
print(chi2, ", ", p)


# Llama-7b::second run
print("Chi-squared test results for Llama-7b, second run:")

# Pair 1: female (404, 0.403) vs male (404, 0.297)
chi2, p = chi_squared_proportions(0.403, 404, 0.297, 404)
print(chi2, ", ", p)

# Pair 2: female (288, 0.816) vs male (288, 0.833)
chi2, p = chi_squared_proportions(0.816, 288, 0.833, 288)
print(chi2, ", ", p)

# Pair 3: female (348, 0.405) vs male (348, 0.259)
chi2, p = chi_squared_proportions(0.405, 348, 0.259, 348)
print(chi2, ", ", p)

# Pair 4: female (235, 0.396) vs male (235, 0.289)
chi2, p = chi_squared_proportions(0.396, 235, 0.289, 235)
print(chi2, ", ", p)

# Pair 5: female (350, 0.148) vs male (350, 0.063)
chi2, p = chi_squared_proportions(0.148, 350, 0.063, 350)
print(chi2, ", ", p)

# Pair 6: female (309, 0.511) vs male (309, 0.515)
chi2, p = chi_squared_proportions(0.511, 309, 0.515, 309)
print(chi2, ", ", p)


# Llama-7b::third run
print("Chi-squared test results for Llama-7b:")

# Pair 1: female (404, 0.287) vs male (404, 0.135)
chi2, p = chi_squared_proportions(0.287, 404, 0.135, 404)
print(chi2, ", ", p)

# Pair 2: female (288, 0.816) vs male (288, 0.833)
chi2, p = chi_squared_proportions(0.816, 288, 0.833, 288)
print(chi2, ", ", p)

# Pair 3: female (348, 0.394) vs male (348, 0.250)
chi2, p = chi_squared_proportions(0.394, 348, 0.250, 348)
print(chi2, ", ", p)

# Pair 4: female (235, 0.405) vs male (235, 0.289)
chi2, p = chi_squared_proportions(0.405, 235, 0.289, 235)
print(chi2, ", ", p)

# Pair 5: female (350, 0.149) vs male (350, 0.063)
chi2, p = chi_squared_proportions(0.149, 350, 0.063, 350)
print(chi2, ", ", p)

# Pair 6: female (309, 0.525) vs male (309, 0.511)
chi2, p = chi_squared_proportions(0.525, 309, 0.511, 309)
print(chi2, ", ", p)

# Llama-7b::fourth run
print("Chi-squared test results for Llama-7b:")

# Pair 1: female (404, 0.287) vs male (404, 0.135)
chi2, p = chi_squared_proportions(0.287, 404, 0.135, 404)
print(chi2, ", ", p)

# Pair 2: female (288, 0.816) vs male (288, 0.833)
chi2, p = chi_squared_proportions(0.816, 288, 0.833, 288)
print(chi2, ", ", p)

# Pair 3: female (348, 0.394) vs male (348, 0.250)
chi2, p = chi_squared_proportions(0.394, 348, 0.250, 348)
print(chi2, ", ", p)

# Pair 4: female (235, 0.405) vs male (235, 0.289)
chi2, p = chi_squared_proportions(0.405, 235, 0.289, 235)
print(chi2, ", ", p)

# Pair 5: female (350, 0.149) vs male (350, 0.063)
chi2, p = chi_squared_proportions(0.149, 350, 0.063, 350)
print(chi2, ", ", p)

# Pair 6: female (309, 0.525) vs male (309, 0.511)
chi2, p = chi_squared_proportions(0.525, 309, 0.511, 309)
print(chi2, ", ", p)

