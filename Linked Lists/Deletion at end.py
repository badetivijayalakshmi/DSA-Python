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
def del_end(head):
    if head is None:
        print("Empty")
        return None
    if head.next is None:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    return head
        
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    print("LL: ")
    printList(head)
    head = del_end(head)
    print("After deleting")
    printList(head)
    
main()
o/p:
LL: 
10->20->30->Null
After deleting
10->20->Null




