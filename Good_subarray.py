A=list(map(int,input("Enter list value: ").split()))
B=int(input("Enter B value: "))
prefix=[]
temp_add=0
for val in A:
    temp_add+=val
    prefix.append(temp_add)
n=len(A)
result=0
for start in range(n):
    sum_subarray=0
    for end in range(start,n):
        len_subarray=end+1-start+1
        if start==0:
            sum_subarray=prefix[end]
        else:
            sum_subarray=prefix[end]-prefix[start-1]
        
        if len_subarray%2==0 and sum_subarray>B:
            result+=1
        
        if len_subarray%2!=0 and sum_subarray<B:
            result+=1
print(result)

# output:
# Enter list value: 1 2 3 4 5
# Enter B value: 4
# 6

# Explaination:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.