class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(A,B):
    current=A
    count=1

    while current!=None:
        if count==B:
            return current.val
        count+=1
        current=current.next


# Creating a linked list
head = Node(1)
node2 = Node(7)
node3 = Node(5)

head.next = node2
node2.next = node3

# Passing the head to the solve function
print(solve(head,2))

# output:
# 7