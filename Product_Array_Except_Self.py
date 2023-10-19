# Product of Array Except Self

nums = [1,2,3,4]
prefix_mul=[]
temp=1
for val in nums:
  temp*=val
  prefix_mul.append(temp)

suffix_mul=[0]*len(nums)
temp=1
for ind in reversed(range(len(nums))):
  temp*=nums[ind]
  suffix_mul[ind]=temp

l=len(nums)
result=[]
for ind in range(l):
  if ind==0:
    result.append(suffix_mul[ind+1])
  elif ind==l-1:
    result.append(prefix_mul[l-2])
  else:
    temp=prefix_mul[ind-1]*suffix_mul[ind+1]
    result.append(temp)

print(result)


# Output:

# [24, 12, 8, 6]