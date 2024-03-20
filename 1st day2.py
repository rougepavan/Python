def climb_stairs(n):
    ways = [1, 2]
    for i in range(2, n):
        ways.append(ways[i - 1] + ways[i - 2])
    return ways[n - 1]
n = 2
print(f"The number of distinct ways to climb {n} steps is {climb_stairs(n)}.")
