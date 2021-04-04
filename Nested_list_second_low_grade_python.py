''' Given the names and grades for each student in a class,
    store them in a nested list and print the name of any student 
       having the second lowest grade
    If there are multiple students with the second lowest grade, 
       order their names alphabetically and print each name 
'''
my_list=[]
temp_list=[]
n=int(input("Enter the total number of students in class: "))
for i in range(n):  
    name=input("Enter student name: ")
    score=float(input("Enter student mark: "))
    temp_list.append(name)
    temp_list.append(score)
    my_list.append(temp_list)
    temp_list=[] 
sec_lar=[]
name=[]
res=[]
for j in range(n):
  a=my_list[j][1]
  sec_lar.append(a)

sor=set(sec_lar)
sec_lar=list(sor)
sec_lar=sorted(sec_lar)

for j in range(n):
  if sec_lar[1]==my_list[j][1]:
    name.append(my_list[j][0])
    name.append(my_list[j][1])
    res.append(name)
    name=[]
res=sorted(res)
if len(res)<2:
	print("Student with second lowest grade is: ")
else:
	print("Students with second lowest grade are: ")
for j in range(len(res)):
  print(res[j][0])