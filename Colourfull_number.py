def colorful(A):
      A=str(A)
      temp_list=[]
      for val in A:
          temp_list.append(val)
      N=len(temp_list)
      hash_set=set()
      for start in range(N):
          for end in range(start,N):
              prod=1
              for k in range(start,end+1):
                  prod*=int(temp_list[k])
              if prod not in hash_set:
                hash_set.add(prod)
              else:
			            return False
      return True
      

A=3245
print(colorful(A))

# output:

# True

# A number can be broken into different consecutive sequence of digits. 
# The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
# This number is a COLORFUL number, since the product of every consecutive sequence of digits is different