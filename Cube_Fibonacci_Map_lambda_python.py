cube = lambda x:x*x*x 

def fibonacci(n):
    lst=list()
    if n==0:
        a=10
    elif n==1:
        lst.append(0)
    else:
        lst=[0,1]
        i=0
        while len(lst)!=n:
            a=lst[i]+lst[i+1]
            lst.append(a)
            i+=1
    return lst
    
n = int(input("Enter the length: "))
z=fibonacci(n)
print("The Fibonacci series is: ",z)
a=list(map(cube, fibonacci(n)))
print("The Cube of Fibonacci series is: ",a)
