A = [1, 2, 1, 4]
B = [
       [2, 3, 2],
       [1, 4, 5],
       [4, 4, 1]
     ]
temp=[0]*len(A)
for left,right,val in B:
    temp[left-1]+=val
    if right<len(A):
        temp[right]-=val

temp_prefix_sum=[]
temp_val=0
for item in temp:
    temp_val+=item
    temp_prefix_sum.append(temp_val)    
result_array=[]

for ind in range(len(A)):
    temp_val=A[ind]+temp_prefix_sum[ind]
    result_array.append(temp_val)
print("Range sum is: ",result_array)

# output:
# Range sum is:  [6, 9, 8, 10]