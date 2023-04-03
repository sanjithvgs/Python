A=list(map(int,input("Enter building height: ").split()))
n=len(A)
suffix_max=A[:]
for ind in reversed(range(n-1)):
  suffix_max[ind]=max(A[ind],suffix_max[ind+1])
  left_max=0
  total_unit=0
  for ind in range(len(A)):
      left_max=max(A[ind],left_max)
      right_max=suffix_max[ind]
      total_unit+=min(left_max,right_max)-A[ind]
print("Total unit of water trapped in building: ",total_unit)

# output:
# Enter building height: 0 1 0 2
# Total unit of water trapped in building:  1