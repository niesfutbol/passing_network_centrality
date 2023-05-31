import numpy as np

eq = [30, 43, 60, 65, 37, 49, 40, 37, 24, 26, 13, 5, 17, 6, 5]
eq_0 = [30, 43, 60, 79, 37, 49, 40, 37, 24, 26, 13, 5, 3, 6, 5]
eq_1 = [30, 43, 46, 79, 37, 49, 40, 37, 24, 26, 13, 5, 17, 6, 5]
eq_2 = [29, 42, 59, 79, 36, 48, 39, 36, 23, 25, 12, 4, 16, 5, 4]
eq_3 = np.ones(15)

def calculate_simpson(passes_for_team):
    p = np.array(passes_for_team)/np.sum(passes_for_team)
    return np.sum(p*p)

print(f"Simpson para eq {calculate_simpson(eq)}")
print(f"Simpson para eq_0 {calculate_simpson(eq_0)}")
print(f"Simpson para eq_1 {calculate_simpson(eq_1)}")
print(f"Simpson para eq_2 {calculate_simpson(eq_2)}")
print(f"Simpson para eq_3 {calculate_simpson(eq_3)}")

def calculate_centralize(passes_for_team):
    total = np.sum(passes_for_team)
    max_p = np.max(passes_for_team)
    return np.mean([max_p - team for team in passes_for_team])/total

print(f"centralize para eq {calculate_centralize(eq)}")
print(f"centralize para eq_0 {calculate_centralize(eq_0)}")
print(f"centralize para eq_1 {calculate_centralize(eq_1)}")
print(f"centralize para eq_2 {calculate_centralize(eq_2)}")
print(f"centralize para eq_3 {calculate_centralize(eq_3)}")

def calculate_gini_simpson(passes_for_team):
    return 1 - calculate_simpson(passes_for_team)

print(f"Gini-Simpson para eq {calculate_gini_simpson(eq)}")
print(f"Gini-Simpson para eq_0 {calculate_gini_simpson(eq_0)}")
print(f"Gini-Simpson para eq_1 {calculate_gini_simpson(eq_1)}")
print(f"Gini-Simpson para eq_2 {calculate_gini_simpson(eq_2)}")
print(f"Gini-Simpson para eq_3 {calculate_gini_simpson(eq_3)}")

def calculate_shannon(passes_for_team):
    p = np.array(passes_for_team)/np.sum(passes_for_team)
    return -np.sum(p*np.log(p))

print(f"Shannon para eq {calculate_shannon(eq)}")
print(f"Shannon para eq_0 {calculate_shannon(eq_0)}")
print(f"Shannon para eq_1 {calculate_shannon(eq_1)}")
print(f"Shannon para eq_2 {calculate_shannon(eq_2)}")
print(f"Shannon para eq_3 {calculate_shannon(eq_3)}")
