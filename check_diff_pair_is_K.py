# pair A[i]-A[j]==k return True else False   i!=j

def two_pointer_diff(A):
  p1=0
  p2=1
  k=3
  while p2<len(A):
    if A[p2]-A[p1]==k:
      return True
    elif A[p1]-A[p2]>k:
      p1+=1
      if p1==p2:
        p2+=1
    else:
      p2+=1
  return False


A=[-3,0,1,3,6,8,11,14,18,25]
print(two_pointer_diff(A))

# output:
# True