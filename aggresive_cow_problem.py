def aggresive_cow(lst,cow_count):
  l=1
  r=41
  ans=0
  while l<=r:
    mid=(l+r)//2

    if check_possible(lst,mid,cow_count):
      ans=mid
      l=mid+1
    else:
      r=mid-1
  return ans

def check_possible(lst,mid,cow_count):
  current_cow=lst[0]
  cow=1

  for ind in range(1,len(lst)):
    if (lst[ind]-current_cow>=mid):
      cow+=1
      current_cow=lst[ind]
      if cow==cow_count:
        return True
  return False


lst=[2,6,11,14,19,25,30,39,43]
print(aggresive_cow(lst,4))

# output:
# 12

# we can put 4 cows with ditance 12