A = [-7, 1, 5, 2, -4, 3, 0]
count=0
prefix=[]
temp=0
res_ind=len(A)
flag=False
for val in A:
    temp+=val
    prefix.append(temp)
for ind in range(len(prefix)):
    if ind==0:
        lower_ind=0
        higher_ind=prefix[-1]-prefix[0]
    else:
        lower_ind=prefix[ind-1]
        higher_ind=prefix[-1]-prefix[ind]
    if lower_ind==higher_ind:
        if ind<res_ind:
            flag=True
            res_ind=ind
if flag:
  print(res_ind)        
else:
  print(-1)

# output:
# 3

# 3 is an equilibrium index 
# A[0] + A[1] + A[2] = A[4] + A[5] + A[6]