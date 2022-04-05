class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__ (self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data) #allocates the node and puts in data
        new_node.next = self.head #make next of new node as head
        self.head = new_node #move the head to point to the new node

    def deleteLinkedList(self):
        #initialize the current node
        current = self.head
        while current:
            prev = current.next #move next node

            #delete current node
            del current.data

            #set current equals prev node
            current = prev

        """In python, garbage collection happens therefore, only 
            self.head = None 
            would also delete the linkedlist"""


    def countNodes(self):
        """iterative solution on counting nodes:
            a. initialize count as 0
            b. Initialize a node pointer, temp = head
            c. Do following while temp is not NULL
                - temp = temp => next
                - count++
            d. Return count
            """
        temp = self.head #initialize temp
        count = 0 #initailize count

        #loop while end of linkedlist is not reached
        while temp: 
            count +=1
            temp = temp.next
        return count
       

    #prints contents of linkedlist from head
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

#code execution starts here
if __name__ == "__main__":
    llist = linkedList()
    llist.push(4)
    llist.push(6)
    llist.push(7)
    llist.push(9)
    llist.push(14)
    llist.push(24)
    llist.push(33)
    print(f"Linked List created is: ")
    llist.printList()
    print(f"The count of the node is: ", llist.countNodes())

"""    if llist.searchElement(24):
        print(f"Yea")
    else:
        print(f"Not Found")"""
    #print(f"\nLinkedList deleted")
    #llist.deleteLinkedList()