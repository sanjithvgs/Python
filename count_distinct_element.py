A=list(map(int,input("Enter list values: ").split()))
freq_set=set()
for val in A:
  freq_set.add(val)

print("The distinct value count is: ",len(freq_set))


# output:
# Enter list values: 3 3 9 0 1 0
# The distinct value count is:  4