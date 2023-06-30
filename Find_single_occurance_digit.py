def search(lst):
  l=0
  r=len(lst)-1
  first_occur=0

  while l<=r:
    mid=(l+r)//2

    if lst[mid]!=lst[mid+1] and lst[mid]!=lst[mid-1]:
      return lst[mid]
    if lst[mid]==lst[mid+1]:
      first_occur=mid
    elif lst[mid]==lst[mid-1]:
      first_occur=mid-1

    if first_occur%2==0:
      l=mid+1
    else:
      r=mid-1

lst=[9,9,8,8,1,1,3,3,11,6,6,4,4,2,2,5,5]
print(search(lst))

# output:
# 11