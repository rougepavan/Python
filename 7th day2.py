def generate_parentheses(n):
    def backtrack(combination, left, right):
        if len(combination) == 2 * n:
            # If the combination is complete, add it to the result
            result.append(combination)
            return
        if left < n:
            # Add an opening parenthesis if there are remaining left parentheses
            backtrack(combination + '(', left + 1, right)
        if right < left:
            # Add a closing parenthesis if there are more left parentheses than right
            backtrack(combination + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

# Example usage
n = 3
valid_combinations = generate_parentheses(n)
print(f"Valid combinations for {n} pairs of parentheses:")
for combo in valid_combinations:
    print(combo)
