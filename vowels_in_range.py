A="interviewbit"
B=[ [0,4],
 [9,10] ]

result=[]

vowels="aeiou"
prefix=[]
for val in A:
  if val in vowels:
    prefix.append(1)
  else:
    prefix.append(0)

for idx in range(1,len(prefix)):
  prefix[idx]+=prefix[idx-1]

for i in range(len(B)):
  left=B[i][0]
  right=B[i][1]

  if left==0:
    result.append(prefix[right])
  else:
    result.append(prefix[right]-prefix[left-1])

print(result)

# output:

# [1,2]

# The substring for the first query is “inter” which contains 2 vowels.
# The substring for the second query is “bi” which contains 1 vowel.