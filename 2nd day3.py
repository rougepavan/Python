from itertools import permutations
def find_combinations(digits):
    perms = permutations(digits)
    combinations = [''.join(p) for p in perms]
    return combinations
input_digits = "123"
combinations = find_combinations(input_digits)
print("All possible combinations:")
for combo in combinations:
    print(combo)
