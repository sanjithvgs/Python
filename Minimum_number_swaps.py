def swap(A, B):
  n=len(A)
      
  len_B=0
  for j in range(n):
    if A[j]<=B:
      len_B+=1  

      
  non_fav=0
      
  for i in range(len_B):
    if A[i]>B:
      non_fav+=1
      
  i=1
  j=len_B
      
  min_non_fav=non_fav
      
  while j<n-1:
    if A[i-1]>B:
      non_fav-=1
      
    if A[j]>B:
      non_fav+=1

    min_non_fav=min(non_fav,min_non_fav)
    j+=1
    i+=1

  return min_non_fav


A=list(map(int,input("Enter the list element: ").split()))
B=int(input("Enter B value: "))
print("Minimum number of swaps required to bring all the numbers less than or equal to B together is: ",swap(A,B))

# output:
# Enter the list element: 1 12 10 3 14 10 5
# Enter B value: 8
# Minimum number of swaps required to bring all the numbers less than or equal to B together is:  2