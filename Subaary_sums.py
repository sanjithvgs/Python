A=list(map(int,input("Enter list value: ").split()))
print("subaray sum: ")
for start in range(n):
    sum=0
    for ind in range(start,n):
        sum+=A[ind]
        print(sum,end=" ")

# output:
# Enter list value: 1 2 3
# subaray sum: 
# 1 3 6 2 5 3 