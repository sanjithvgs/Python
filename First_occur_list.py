def search(lst,k):
  l=0
  r=len(lst)-1
  ans=0

  while l<=r:
    mid=(l+r)//2
    if lst[mid]==k:
      ans=mid
      r=mid-1

    elif lst[mid]<k:
      l=mid+1
    else:
      r=mid-1
  return ans


lst=[-5,-5,-5,-3,2,3,5,5,5,5,5,7,8,10,12]
print(search(lst,5)) #=>ans =6

# 5 first occur at index: 6