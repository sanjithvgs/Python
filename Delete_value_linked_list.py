The head of a linked list A and an integer B. Delete the B-th node from the linked list.

def solve(A, B):
    current=A

    if B==0:
        A=current.next
        return A
        
    while B!=1 and current.next!=None:
        B-=1
        current=current.next

    current.next=current.next.next
    return A

Input:
A = 4 -> 3 -> 2 -> 1
B = 0

output:
3 -> 2 -> 1