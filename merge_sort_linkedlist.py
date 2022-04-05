class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def mergeSort(head):
    if head.next == None:
        return head
    

def printList(head):
    if head is None:
        return
    while head:
        print(head.data, end = " ")
        head = head.next

head = Node(10)
temp = head
temp.next = Node(2)
temp = temp.next
temp.next = Node(9)
temp = temp.next
temp.next = Node(5)
temp = temp.next
temp.next = Node(7)
temp = temp.next
temp.next = Node(4)
#temp = temp.next
printList(head)