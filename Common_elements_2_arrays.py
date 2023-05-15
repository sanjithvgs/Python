A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
freq_A={}
freq_B={}       
for val in A:
  if val in freq_A:
    freq_A[val]+=1
  else:
    freq_A[val]=1
for val in B:
  if val in freq_B:
    freq_B[val]+=1
  else:
    freq_B[val]=1      
M=len(A)
N=len(B)        
result_list=[]        
if M>=N:
  for val in A:
    if val in freq_B:
      result_list.append(val)
      if freq_B[val]>1:
        freq_B[val]-=1
      else:
        del freq_B[val]        
else:
  for val in B:
    if val in freq_A:
      result_list.append(val)
      if freq_A[val]>1:
        freq_A[val]-=1
      else:
        del freq_A[val]
print("The common elements in both array are: ",result_list)

# output:
# The common elements in both array are:  [1, 2, 2]