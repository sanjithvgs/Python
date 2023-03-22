A = [2, 1, 8, 3, 9, 6]
B = [   [0, 3],
        [3, 5],
        [1, 3],
        [2, 4]   ]
prefix=[]
even_sum=0
for val in A:
    if val%2==0:
        even_sum+=1
    else:
        even_sum+=0
    prefix.append(even_sum)
result=[]
for ind in range(len(B)):
    left=B[ind][0]
    right=B[ind][1]
    if left==0:
        result.append(prefix[right])
    else:
        result.append(prefix[right]-prefix[left-1])
print("Even number count in give ranges are: ",result)

# output:
# Even number count in give ranges are:  [2, 1, 1, 1]


# The subarray for the first query is [1, 2, 3] (index 0 to 2) which contains 1 even number.
# The subarray for the second query is [3, 4, 5] (index 2 to 4) which contains 1 even number.
# The subarray for the third query is [2, 3, 4, 5] (index 1 to 4) which contains 2 even numbers.