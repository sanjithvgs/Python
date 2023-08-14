class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    if not head:
        return None

    seen = set()
    current = head
    previous = None

    while current:
        if current.val in seen:
            previous.next = current.next
        else:
            seen.add(current.val)
            previous = current
        current = current.next

    return head

# Example usage
# Create an unsorted linked list: 1 -> 3 -> 2 -> 1 -> 4 -> 3 -> 5
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(5)

new_head = remove_duplicates(head)

# Print the modified linked list: 1 -> 3 -> 2 -> 4 -> 5
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next


# output:
# 1 -> 3 -> 2 -> 4 -> 5 -> 