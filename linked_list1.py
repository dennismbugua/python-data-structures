class Node: 
    #Initializes the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #initializing the head function
    def __init__(self):
        self.head = None

    def printNthFromLast(self, n):
        """Maintain two pointers – reference pointer and main pointer. 
        Initialize both reference and main pointers to head. 
        First, move the reference pointer to n nodes from head. 
        Now move both pointers one by one until the reference pointer reaches the end. 
        Now the main pointer will point to nth node from the end. 
        Return the main pointer."""
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if (self.head is not None):
            while count < n:
                if ref_ptr:
                    print(f"greater than no. of nodes")
                    return

                ref_ptr = ref_ptr.next
                count += 1

        if ref_ptr:
            self.head = self.head.next
            if self.head:
                print(f"Node number is: ", n, main_ptr.data)
        else:
            while (ref_ptr is not None):
                main_ptr = main_ptr.next
                ref_ptr = ref_ptr.next
            print(f"Node from last is: ", n, main_ptr.data)

    #prints the contents of the linked list from head
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

#code execution starts here
if __name__ == '__main__':

    #start with an empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second #links head to the second node
    second.next = third #lists second node with third node

    llist.printList()

    llist.printNthFromLast(3)
