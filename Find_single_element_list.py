#Every element occur twice except one element, find that element without using extra space.
nums = [4,1,2,1,2]

result=0

for val in nums:
  result^=val

print(result)

# output:
# 4