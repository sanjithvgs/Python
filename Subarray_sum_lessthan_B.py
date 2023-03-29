A=list(map(int,input("Enter list value: ").split()))
B=int(input("Enter B value: "))
n=len(A)
result=0
prefix=[]
sum=0
for val in A:
    sum+=val
    prefix.append(sum)
for start in range(n):
    for end in range(start,n):
        if start==0:
            total=prefix[end]
        else:
            total=prefix[end]-prefix[start-1]
        if total<B:
            result+=1
print("Number of subarrays in A having sum less than B: ",result)

# output:
# Enter list value: 1 11 2 3 15
# Enter B value: 10
# Number of subarrays in A having sum less than B:  4
