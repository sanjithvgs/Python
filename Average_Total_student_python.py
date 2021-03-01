# Find Average , Total of student
# Display number of subject got Failed
def fun(dic,num):
  total=0
  count=0
  grade= "True"
  for j in range(num):
    total=dic[j]+total
  avg=total/num
  for j in range(num):
    if dic[j]<30:
      grade= "False"
      count+=1
  print("Average of all subject is:",avg)
  print("Total of all subject is:",total)
  if(grade=="True"):
    print("Student is Pass in all subjects")
  else:
    print("The student Fails in",count,"subjects")


num=int(input("Enter the number of subjects:"))
dic1={ }
for i in range(num):
  a=int(input("Enter a Mark: "))
  dic1[i]=a
fun(dic1,num)