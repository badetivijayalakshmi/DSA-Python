class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def print_list(head):
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("Null")
    
def insert_b(head,x):
    new_node = Node(x)
    new_node.next = head
    return new_node
    
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    print("Original LL:")
    print_list(head)
    head = insert_b(head,1)
    print("After insertion:")
    print_list(head)
main()
o/p:
Original LL:
10->20->30->Null
After insertion:
1->10->20->30->Null
