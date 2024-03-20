def num_good_pairs(nums):
    freq_map = {}
    good_pairs = 0
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    for freq in freq_map.values():
        good_pairs += (freq * (freq - 1)) // 2
    return good_pairs
nums = [1, 2, 3, 1, 1, 3]
print(f"Number of good pairs: {num_good_pairs(nums)}")
