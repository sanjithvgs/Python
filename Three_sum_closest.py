def threeSumClosest(A, B):
    A.sort()
    n = len(A)
    best_sum = float('inf')
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            temp_sum = A[i] + A[j] + A[k]
            if temp_sum == B:
                return B
            if abs(temp_sum - B) < abs(best_sum - B):
                best_sum = temp_sum
            if temp_sum < B:
                j += 1
            else:
                k -= 1
    return best_sum

A = [-1, 2, 1, -4]
B = 1
print(threeSumClosest(A,B))

# output:
# 2

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)