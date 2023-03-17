A=list(map(int,input("Enter stock value for each day: ").split()))
min_val=float('inf')
max_profit=0
for i in range(len(A)):
    if A[i]<min_val:
        min_val=A[i]
    elif ((A[i]-min_val)>max_profit):
        max_profit=A[i]-min_val
print("Maximum profit was: ",max_profit)

# output:
# Enter stock value for each day: 1 4 5 2 4
# Maximum profit was:  4

# Buy the stock on day 0, and sell it on day 2