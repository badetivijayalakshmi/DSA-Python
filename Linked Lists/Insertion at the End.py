class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("Null")


def insert_end(head, x):
    new_node = Node(x)

    # Case 1: Empty list
    if head is None:
        return new_node

    # Case 2: Traverse to last node
    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    return head


# Main
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    print("LL:")
    print_list(head)

    head = insert_end(head, 50)

    print("After insertion:")
    print_list(head)


main()
o/p:LL: 
10->20->30->Null
After insertion: 
10->20->30->50->Null


