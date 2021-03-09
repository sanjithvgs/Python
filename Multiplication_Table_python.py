tab=int(input("Enter Table number: "))
cnt_strt=int(input("Enter Table Starting range: "))
cnt=int(input("Enter Table Ending range: "))

for i in range(cnt_strt,cnt+1):
  res=tab*i
  print(tab,"x",i,"=",res)
