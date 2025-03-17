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

    # Step 4: Process groups of k nodes
    while count >= k:
        prev = None
        current = prev_group_end.next

        # Step 5: Reverse k nodes
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 6: Connect the reversed group
        temp = prev_group_end.next  # Store old head (which is now the end)
        prev_group_end.next = prev  # Connect previous part to new head
        temp.next = current  # Connect the old head to the remaining list

        # Step 7: Move to the next group
        prev_group_end = temp
        count -= k
