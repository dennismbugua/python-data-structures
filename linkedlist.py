class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
        # self.value = value

    def printList(self):
        node = self.head
        while node:
            print (node.data, end = " ")
            node = node.next

#test case
root = LinkedList()
root.head = Node(3)
second = Node(5)
third = Node(7)
forth = Node(9)

root.head.next = second
second.next = third
third.next = forth

root.printList()

    # root.head.next = Node(5)
    # root.head.next.next = Node(6)
    # root.printList()