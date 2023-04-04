A=list(map(int,input("Enter a value of list: ").split()))
n=len(A)
res_sum=0
maxi=-float('inf')
for val in A:
    res_sum+=val
    if res_sum>maxi:
        maxi=res_sum
    if res_sum<0:
        res_sum=0

print("Maximum subarray sum: ",maxi)
    
# output:
# Enter a value of list: -2 1 -3 4 -1 2 1 -5 4
# Maximum subarray sum:  6
