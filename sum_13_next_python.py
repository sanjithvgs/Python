
def sum13(nums):
  i=0
  cnt=0
  while i is not len(nums):
    if nums[i]==13:
      if i==len(nums)-1:
        nums.remove(nums[i])
      else:
        nums.remove(nums[i])
        nums.remove(nums[i])
    else:
      i+=1
  print("List without element 13 and next element of 13 is:",end="")
  print(lst)
  for j in range(len(nums)):
    cnt+=nums[j]
  print("The sum of new List is: ",end="")
  return cnt

lst=[]
l=int(input("Enter the length: "))
for i in range(l):
  a=int(input("Enter the element: "))
  lst.append(a)
print(sum13(lst))