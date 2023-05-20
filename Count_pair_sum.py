def solve(A, B):
  freq_dict={}
  result_count=0
  for ind in range(len(A)):
      if B-A[ind] in freq_dict:
          result_count+=freq_dict[B-A[ind]]            
      if A[ind] in freq_dict:
          freq_dict[A[ind]]+=1
      else:
          freq_dict[A[ind]]=1               
  return result_count % (10**9 + 7)

A = [1, 2, 1, 2]
B = 3
print("The count of give pair sum is: ",end="")
print(solve(A,B))

# output:
# The count of give pair sum is: 4
      
# The pair which gives sum as 3 are (1, 2), (1, 4), (2, 3) and (3, 4). 