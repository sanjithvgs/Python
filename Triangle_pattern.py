cnt=int(input())
for i in range(cnt,0,-1):
  for j in range(i):
    print(" ",end="")
  print("* "*(cnt-j))