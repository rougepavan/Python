def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate the area between the two pointers
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        # Move the pointer with smaller height towards the other pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # Output: 49
