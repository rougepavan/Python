def add_binary(a, b):
    carry = 0
    result = []
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        total = digit_a + digit_b + carry
        carry = total // 2
        result.append(str(total % 2))
        i -= 1
        j -= 1
    return ''.join(result[::-1])
a = "11"
b = "1"
print(f"Sum of {a} and {b} in binary: {add_binary(a, b)}")
