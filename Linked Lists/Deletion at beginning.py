class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printList(head):
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next
    print("Null")
def del_begin(head):
    if head is None:
        print("Empty")
        return None
    return head.next
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    print("LL: ")
    printList(head)
    head = del_begin(head)
    print("After deleting")
    printList(head)
    
main()
o/p:LL: 
10->20->30->Null
After deleting
20->30->Null
