def max_guests_at_any_instance(T, E, L):
    max_guests = 0
    current_guests = 0

    
    for i in range(T):
        
        current_guests += E[i] - L[i]

        
        max_guests = max(max_guests, current_guests)

    return max_guests


T = 5
E = [0, 2, 5, 3, 1]
L = [0, 1, 3, 2, 0]
print(max_guests_at_any_instance(T, E, L))  # Output: 5
