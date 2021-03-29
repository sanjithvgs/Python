def big_diff(nums):
  big=0
  for i in range(len(nums)-1):
    if nums[i+1]>nums[i] and nums[i+1]>big:
      big=nums[i+1]
  big=max(big,nums[0])
  small=big
  for i in range(len(nums)-1):
    if nums[i]>nums[i+1] and nums[i+1]<small:
      small=nums[i+1]
  small=min(small,nums[0])
  return big-small

nums=[]
le=int(input("Enter the length of list: "))  
for i in range(le):
  a=int(input("Enter a element: "))
  nums.append(a)
print("The difference between largest and smallest value is: ",end="")
print(big_diff(nums))
