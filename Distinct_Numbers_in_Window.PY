def dNums(A, B):
      hash_map={}
      result_list=[]
      for ind in range(B):
          if A[ind] in hash_map:
              hash_map[A[ind]]+=1
          else:
              hash_map[A[ind]]=1
      result_list.append(len(hash_map))
      start=0
      end=B
      while end<len(A):
          if hash_map[A[start]]<2:
              del hash_map[A[start]]
          else:
              hash_map[A[start]]-=1
          if A[end] not in hash_map:
              hash_map[A[end]]=1
          else:
              hash_map[A[end]]+=1
          result_list.append(len(hash_map))
          start+=1
          end+=1
      return result_list

A = [1, 2, 1, 3, 4, 3]
B = 3
print(dNums(A,B))

output:
[2, 3, 3, 2]

#  A=[1, 2, 1, 3, 4, 3] and B = 3
#  All windows of size B are
#  [1, 2, 1]
#  [2, 1, 3]
#  [1, 3, 4]
#  [3, 4, 3]
#  So, we return an array [2, 3, 3, 2].