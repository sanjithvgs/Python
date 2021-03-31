'''  Return the sum of list 
     Except ignore sections of numbers starting with a 6 and extending to the next 7
'''
def sum67(nums):
  i=0
  cnt=0
  while i!=len(nums):
    if nums[i]==6:
      while i!=len(nums):
        if nums[i]==7:
          nums.remove(nums[i])
          break
        else:
          nums.remove(nums[i])
    else:
      i+=1
  print("The list without the section from 6 to 7 is: ",lst)
  for i in range(len(nums)):
    cnt+=nums[i]
  print("The sum of list without the section from 6 to 7 is: ",end="")
  print(cnt)

lst=[]
l=int(input("Enter the length: "))
for i in range(l):
  a=int(input("Enter the element: "))
  lst.append(a)

sum67(lst)