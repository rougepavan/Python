from collections import defaultdict
def group_anagrams(strs):
    temp = defaultdict(list)
    for word in strs:
        temp[str(sorted(word))].append(word)
    return list(temp.values())
input_strs = ["eat","tea","tan","ate","nat","bat"]
grouped_anagrams = group_anagrams(input_strs)
print("The grouped Anagrams:")
for group in grouped_anagrams:
    print(group)
