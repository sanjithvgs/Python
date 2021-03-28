'''  
     Return True if the given string contains an appearance of "xyz" 
     where the xyz is not directly preceeded by a period (.)
     So "xxyz" counts but "x.xyz" does not
'''

def xyz_there(str):
  a="xyz"
  z=".xyz"
  b=True
  c=len(str)
  if len(str)<=2:
    b=False
  else:  
    for i in range(c-2):
      if str[i:i+3]==a:
        if str[i-1:i+3]==z:
          b=False
        else:
          b=True
      elif str[i:i+3]!=a:
        c-=1
  if c<=2 or b==False or len(str)<=2:
    print(str+"-->False")
  else:
  	print(str+"-->True")

xyz_there('abcxyz') 
xyz_there('abc.xyz')
xyz_there('xyz.abc')
xyz_there('abcxy')
xyz_there('xyz')
xyz_there('xy') 
xyz_there('x')
xyz_there('') 
xyz_there('abc.xyzxyz') 