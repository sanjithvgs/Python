from functools import cmp_to_key
def compare(a,b):
  s1=str(a)
  s2=str(b)
  if ((s1+s2)<(s2+s1)):
    return 1
  else:
    return -1

A=[33,453,456,98,202]
A.sort(key=cmp_to_key(compare))
print(A)

# output:
# [98, 456, 453, 33, 202]