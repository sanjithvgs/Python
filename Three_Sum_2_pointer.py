# find all such unique triplets a, b, c in A such that a + b = - c.

def threeSum(A):
      A = sorted(A)
      ans = []        
      for i in range(len(A)-2):
          # to avoid duplicate triplet
          if i > 0 and A[i] == A[i-1]:
              continue        
          j = i + 1
          k = len(A) - 1
          target = -(A[i]) 
          while j < k:
              cur_sum =  A[j] + A[k]
              if cur_sum == target:
                  triplet = [-target,A[j],A[k]]
                  ans.append([-target,A[j],A[k]])
                  # another conditional for not calculating duplicates
                  while j < k and A[j] == A[j+1]:
                      j += 1                      
                  while j < k and A[k] == A[k-1]:
                      k -= 1
                  j = j + 1
                  k = k - 1                    
              if cur_sum < target:
                  j = j + 1
              elif cur_sum > target:
                  k = k - 1
      return ans

A = [-1, 0, 1, 2, -1, 4]
print(threeSum(A))

# output:
# [[-1, -1, 2], [-1, 0, 1]]