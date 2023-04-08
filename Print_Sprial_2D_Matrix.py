array=[
    [8, 2, 5], 
    [2, 9, 6], 
    [5, 8, 7] ]
n=len(array)

x=0
y=0
direction="right"
boundry=0
count=0
while count<n*n:
    count+=1
    print(array[x][y],end=" ")
    if direction=="right":
        y+=1
        if y==n-1-boundry:
            direction="down"
        
    elif direction=="down":
        x+=1
        if x==n-1-boundry:
            direction="left"

    elif direction=="left":
        y-=1
        if y==boundry:
            direction="top"
    
    elif direction=="top":
        x-=1
        if x==boundry+1:
            direction="right"
            boundry+=1

# output:

# 8 2 5 6 7 8 5 2 9 