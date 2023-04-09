def average(A, B):
    n=len(A)
    init_sum=0
    for ind in range(B):
        init_sum+=A[ind]
    min_average=init_sum/B
    current_sum=init_sum
    result_index=0
    for start in range(1,n-B+1):
        end=start+B-1
        current_sum+=A[end]
        current_sum-=A[start-1]
        temp=current_sum/B
        if temp<min_average:
            min_average=temp
            result_index=start
    return result_index

A=list(map(int,input("Enter the list element: ").split()))
B=int(input("Enter the length: "))
print("Least average:",average(A,B))

# output:
# Enter the list element: 3 7 90 20 10 50 40
# Enter the length: 3
# Least average: 3