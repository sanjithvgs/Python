
'''  Make a package of goal kilos of chocolate
     We have small bars (1 kilo each) and big bars (5 kilos each)
     Return the number of small bars to use, 
     assuming we always use big bars before small bars
     Return Number of small bars is needed
'''

def make_chocolate(small, big, goal):
  l_c=goal//5
  cnt=0
  a=0
  if(l_c>big):
    l_c=big
  z =l_c*5
  if z==goal:
    cnt=0
 
  else:
    for i in range(small):
      if z<=0:
        cnt=0
      else:
        z=z+1
        cnt+=1
        if (z==goal):
          break
  
  if z!=goal:
    cnt=-1

  if cnt<0:
    if(small==goal):
      return small
    return -1
  else:
    return cnt

small=int(input("Enter the number of Small bars: "))
big=int(input("Enter the number of Big bars: "))
goal=int(input("Enter the goal of chocolate in kilos: "))
m=make_chocolate(small,big,goal)
if m<=0:
	print("No Small bars are needed..!")
else:
	print("The total number of Small bars are needed is",m)