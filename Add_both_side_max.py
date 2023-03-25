A=list(map(int,input("Enter the list value: ").split()))
B=int(input("Enter the range to pick from both side: "))
n=len(A)
init_sum=0
for ind in range(B):
  init_sum+=A[ind]

max_sum=init_sum

left=B-1
right=n-1
curr_sum=init_sum
for left_ind in range(left,-1,-1):
  curr_sum-=A[left_ind]
  curr_sum+=A[right]
  max_sum=max(max_sum,curr_sum)
  right-=1

print("The maximum sum pick from both sides are: ",max_sum)

# output:
# Enter the list value: 5 -2 3 1 2
# Enter the range to pick from both side: 3
# The maximum sum pick from both sides are:  8

#  Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8