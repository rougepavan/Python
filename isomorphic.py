def isomorphic(s1, t1):
    if len(s1) != len(t1):
        return False
    
    mapping = {}
    for i in range(len(s1)):
        if s1[i] not in mapping:
            if t1[i] in mapping.values():
                return False
            mapping[s1[i]] = t1[i]
        elif mapping[s1[i]] != t1[i]:
            return False
    
    return True

# Example usage:
s1 = input("Enter the first string: ")
t1 = input("Enter the second string: ")
print(isomorphic(s1, t1))

s2 = input("Enter the first string: ")
t2 = input("Enter the second string: ")
print(isomorphic(s2, t2))
