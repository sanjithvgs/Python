def solve(A):
    freq_first={}
    for val in A:
        if val in freq_first:
            freq_first[val]+=1
        else:
            freq_first[val]=1
    min_index=float('inf')
    check_flag=False
    for i in range(len(A)):
        if freq_first[A[i]]>1:
            min_index=min(i,min_index)
            check_flag=True
    if check_flag:
        return A[min_index]
    return -1

A = [10, 5, 3, 4, 3, 5, 6]
print("First repeating element in list is: ")
print(solve(A))

# output:
# First repeating element in list is: 
# 5