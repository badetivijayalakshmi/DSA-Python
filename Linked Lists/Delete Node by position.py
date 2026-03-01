class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("Null")


def delete_at_position(head, pos):
    
    # Case 1: Invalid position or empty list
    if head is None or pos < 1:
        return head
    
    # Case 2: Delete first node
    if pos == 1:
        return head.next
    
    temp = head
    
    # Move to (pos - 1)th node
    for i in range(1, pos - 1):
        if temp.next is None:
            return head  # Position out of range
        temp = temp.next
    
    # If position is out of range
    if temp.next is None:
        return head
    
    # Skip the node to be deleted
    temp.next = temp.next.next
    
    return head


# Driver Code
if __name__ == "__main__":
    
    # Creating: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original List:")
    printList(head)

    # Delete node at position 3
    head = delete_at_position(head, 3)

    print("After Deleting Position 3:")
    printList(head)
o/p:
Original: 
1->2->3->4->null
After deletion: 
1->2->4->null
