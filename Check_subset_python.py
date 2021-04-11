'''  
    Check whether the subset is avialble in another list
'''

import itertools    
n=int(input("Enter the number of time: "))
lst5=[]
for _ in range(n):
    leng=int(input("Enter the length of first list: "))
    lst =list(map(int, input("Enter the element: ").split()))
    leng2=int(input("Enter the length of second list: "))
    lst2 =list(map(int, input("Enter the element: ").split()))
    res=False
    if leng>leng2:
      data = [x for x in itertools.combinations(lst, leng2) ]
      for item in data:
        item = list (item)
        if item==lst2:
          res=True
    else:
      data = [x for x in itertools.combinations(lst2, leng) ]
      for item in data:
        item = list (item)
        if item==lst:
          res=True
    print(res)  