# question:
# Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

A = [1, 2, 2, 3, 1]
result=0
for i in range(len(A)):
    result=result^A[i]

print(result)

# output:3