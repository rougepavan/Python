def count_sorted_vowel_strings(n):
    
    dp = [[0] * 5 for _ in range(n + 1)]

    
    for j in range(5):
        dp[1][j] = 1

    
    for i in range(2, n + 1):
        for j in range(5):
            
            for k in range(j + 1):
                dp[i][j] += dp[i - 1][k]

   
    total_count = sum(dp[n])
    return total_count


n = 2
print(count_sorted_vowel_strings(n))  
