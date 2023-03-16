A=list(map(int,input("Enter list value as 0 or 1: ").split()))
res_count=0
check_flag=True
for i in range(len(A)):
  if check_flag:
    if A[i]==0:
      res_count+=1
      check_flag=False
  else:
    if A[i]==1:
      res_count+=1
      check_flag=True
print("Minimum number of switches required are: ",res_count)

# output:
# Enter list value as 0 or 1: 0 1 0 1
# Minimum number of switches required are:  4


#  press switch 0 : [1 0 1 0]
#  press switch 1 : [1 1 0 1]
#  press switch 2 : [1 1 1 0]
#  press switch 3 : [1 1 1 1]