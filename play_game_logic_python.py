'''
Able to play game or not
play if the temperature is between 60 and 90 
Unless it is summer, then the upper limit is 100 instead of 90
Given an int temperature and a boolean is_summer,
Return the result
'''

def play(temp, is_summer):
  if temp>=60 and temp<=90:
    return True
  elif is_summer:
    if temp>=60 and temp<=100:
      return True
    else:
      return False
  else:
    return False
try:
	a=int(input("Enter the temperature (in number): "))
	b=input("Enter if it is summer or not (True/False): ")
	z=play(a,b)
	if z:
		print("Able to play Game..")
	else:
		print("Not able to play Game..")
except:
	print("Invalid Input..!")