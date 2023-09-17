# Given a singly linked list A

#  A: A0 → A1 → … → An-1 → An 
# reorder it to:

#  A0 → An → A1 → An-1 → A2 → An-2 → … 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderLinkedList(head):
    if not head or not head.next:
        return head

    # Step 1: Find the middle of the linked list using the two-pointer technique.
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves.
    second_half = slow.next
    slow.next = None

    # Step 2: Reverse the second half of the linked list.
    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Merge the two halves in the required order.
    first_half = head
    second_half = prev
    while second_half:
        next_first = first_half.next
        next_second = second_half.next

        first_half.next = second_half
        second_half.next = next_first

        first_half = next_first
        second_half = next_second

    return head
