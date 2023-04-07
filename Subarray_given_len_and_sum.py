def solve(A, B, C):
    n=len(A)
    prefix_sum=[]
    temp=0
    for val in A:
        temp+=val
        prefix_sum.append(temp)
    
    initial_sum=prefix_sum[B-1]
    if initial_sum==C:
        return 1

    result_sum=0
    for start in range(1,n-B+1):
        end=start+B-1
        if start==0:
            result_sum=prefix_sum[end]
        else:
            result_sum=prefix_sum[end]-prefix_sum[start-1]
        if result_sum==C:
            return 1
        result_sum=0
    return 0

A = [4, 3, 2, 6, 1]
B = 3
C = 11
print(solve(A,B,C))

# output:
# 1    Subarray with len B having Sum C is present
