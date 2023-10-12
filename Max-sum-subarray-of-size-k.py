lst=  [2, 1, 5, 1, 3, 2]
k=4

prefix=[]
temp=0
for val in lst:
  temp+=val
  prefix.append(temp)
  # [2, 3, 8, 9, 12, 14]

first=prefix[k-1]
max_sum=first

i=k
while i<len(lst):
  current_sum=prefix[i]-prefix[i-k]
  if current_sum>max_sum:
    max_sum=current_sum
  i+=1

print(max_sum)

# output:
# 11


# The subarray [5, 1, 3, 2] has the maximum sum of 11.