# Duplicate the value
# Remove uppercase letter,
# if vowels means replace with #
def solve(A):
    A=A+A
    vowels=["a","e","i","o","u"]
    A=list(A)
    ind=0
    while ind<len(A):
        if A[ind].isupper():
            del A[ind]
        elif A[ind] in vowels:
            A[ind]="#"
        ind+=1
    res=""
    for val in A:
        res+=val
    return res

A='hgUe'
print(solve(A))

# output:
# hgehge