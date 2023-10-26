A = [5, 6, 10,-1, 7, 8, 10]

start=0
end=0
max_len=0
best_start=0
best_end=0

while end<len(A):

  while start<len(A) and A[start]<1: #Find Start
    start+=1

  end=start
  while end<len(A) and A[end]>=0: #Find end of subarray
    end+=1

  temp_len=(end-1)-(start)+1  #check maximum
  if temp_len>max_len:
    max_len=temp_len
    best_start=start
    best_end=end-1

  start=end+1   #Again move start to next subarray

print(A[best_start:best_end+1])

# output:

# [5, 6, 10]

#  There are two subarrays of size 3 having only non-negative elements.
#  1. [5, 6, 10] starting point = 0
#  2. [7, 8, 10] starting point = 4
#  As staring point of 1 is smaller, return [5, 6, 10]