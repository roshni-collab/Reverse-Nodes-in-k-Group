class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if not head or k == 1:
        return head  # No need to reverse if k is 1 or list is empty

    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    # Step 3: Initialize dummy node and pointers
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
