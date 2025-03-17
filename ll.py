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
    
     # Step 8: Return new head
    return dummy.next


# Example Test Cases
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


# Creating a sample linked list [1,2,3,4,5]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5    

# Running the function with k = 2 and k = 3
print_list(reverseKGroup(node1, 2)) 

# Resetting the list to [1,2,3,4,5]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_list(reverseKGroup(node1, 3)) 