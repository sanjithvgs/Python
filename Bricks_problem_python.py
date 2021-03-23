'''To make a row of bricks that is goal inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each)
    Return True if it is possible to make the goal by choosing from the given bricks
'''
def make_bricks(small, big, goal):
  lb=goal//5
  if lb>big:
    lb=big
  goal = goal-(lb*5)
  if small>=goal:
    print("Bricks are sufficient...")
  else:
  	print("Bricks are Insufficient..! ")

s_b=int(input("Enter the count of small bricks: "))
l_b=int(input("Enter the count of large bricks: "))
goal=int(input("Enter a goal long in inches: "))
make_bricks(s_b,l_b,goal)