# pair A[i]+A[j]==k return True else False   i!=j

def two_pointer(A):
  p1=0
  p2=len(A)-1
  k=30
  while p1<p2:
    if A[p1]+A[p2]==k:
      return True
    elif A[p1]+A[p2]>k:
      p2-=1
    else:
      p1+=1
  return False


A=[-3,0,1,3,6,8,11,14,18,25]
print(two_pointer(A))

# output:
# False