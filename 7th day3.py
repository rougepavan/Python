def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(tuple(nums[:]))
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[start]:
                continue
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            nums.sort()  
    result = []
    backtrack(0)
    return result
input_nums = [1, 1, 2]
unique_permutations = permute_unique(input_nums)
print("Unique permutations:")
for perm in unique_permutations:
    print(perm)
