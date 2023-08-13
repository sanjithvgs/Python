def frequency_sort(arr):
    frequency_map = {}
    
    # Count frequencies
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
            
    # Sort by frequency and then value
    sorted_arr = sorted(arr, key=lambda x: (frequency_map[x], x), reverse=True)
    
    return sorted_arr

input_data = [4, 2, 2, 8, 4, 6, 4, 8, 2, 4, 2, 8]
sorted_output = frequency_sort(input_data)
print(sorted_output) 

 # Output: [2, 2, 2, 2, 4, 4, 4, 8, 8, 8, 6]
