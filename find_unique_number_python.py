def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([5,7,7,8,5,1,2,2,2,2])) 