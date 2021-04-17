s = list(map(int, input("Enter the number of student and number of subject: ").split()))
lst=[]
temp=[]
res=[]
i=0
z=0
for _ in range(s[1]):
  print("Enter a marks of a student: ")
  lst += list(map(float, input().split()))

for j in range(s[1]):
  b=s[0]
  a=lst[i:i+b]
  temp.append(a)
  i+=b
for n in range(s[0]):
  for m in range(s[1]):
    z+=temp[m][n] 
    c=z/s[1]
    res.append(c)

print("The average of each subject for all student is: ")
for item in res:
  print(item)