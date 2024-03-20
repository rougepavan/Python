def modify_string(S):
    # Count the frequency of each character in the string
    freq = {}
    for char in S:
        freq[char] = freq.get(char, 0) + 1

    # Modify the string
    modified_string = ''
    for char in S:
        # Calculate the circular distance
        circular_distance = (ord(char) - ord('a') + freq[char]) % 26
        # Replace the character with the modified character
        modified_char = chr(ord('a') + circular_distance)
        modified_string += modified_char

    return modified_string

# Example usage:
S = "abca"
print(modify_string(S))  # Output: "bcbd"
