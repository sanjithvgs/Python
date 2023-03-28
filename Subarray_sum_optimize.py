A=list(map(int,input("Enter list value: ").split()))
n=len(A)
summ=0
for i in range(len(A)):
    summ+=A[i]*((i+1)*(n-i))
print("The subarray sum: ",summ)

# output:
# Enter list value: 1 2 3 4 5
# The subarray sum:  105