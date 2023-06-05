def num(N):
    if N==1:
        print(1,end=" ")
        return
    num(N-1)
    print(N,end=" ")

N=int(input("Enter the number: "))
num(N)
print()