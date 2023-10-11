string="   fly me   to   the moon       "
n=len(string)
i=0
length=0
while i<n-1 and string[i]==' ':
  i-=1

while i<n-1 and string[i]!=' ':
  length+=1
  i-=1

print(length)


# output: 4