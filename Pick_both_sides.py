a=[3,1,2,1,6,9]
B=3
curr_sum=0
l=len(a)
for ind in range(B):
  curr_sum+=a[ind]

max_sum=curr_sum
right_idx=l-1
B=B-1
while B>=0:
  curr_sum-=a[B]
  curr_sum+=a[right_idx]
  B-=1
  right_idx-=1
  max_sum=max(curr_sum,max_sum)

print(max_sum)

# output:
# 18

# left=>3
# right=>6,9
# 3+6+9 => 18