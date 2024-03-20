def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0
    jumps = 0
    curr_max_reach = nums[0]
    next_max_reach = nums[0]
    for i in range(1, n):
        if i > curr_max_reach:
            curr_max_reach = next_max_reach
            jumps += 1
        next_max_reach = max(next_max_reach, i + nums[i])
        if curr_max_reach >= n - 1:
            return jumps + 1
    return -1
nums = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(f"Minimum number of jumps: {min_jumps(nums)}")
