''' Given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
    Print a list of all possible coordinates given by (x,y,z) on a 3D grid 
    where the sum of i+j+k is not equal to n'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
templst=[]
lst=[]
for a in range(x+1):
    for b in range(y+1):
       for c in range(z+1):
            if a+b+c!=n:
                templst.append(a)
                templst.append(b)
                templst.append(c)
                lst.append(templst)
            templst=[]
print(lst)                
