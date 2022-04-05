class Node:
    #initializing node object
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    #initailizing linkedlist object
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """4 steps to adding a node at the front:
            a. allocate the node and put in the data
            b. make next of new node as head
            c. move the node to point to the new node"""
        new_node = Node(new_data) #allocate the node and put in the data
        new_node.next = self.head #make next of new node as head
        self.head = new_node #move the node to point to the new node




            #function to alternate odd and even nodes
    def rearrange(head):
        #Step 1: Segregate Odd and even values
        temp = head.next
        prev_temp = head

        while temp:
            #backup next pointer of temp
            x = temp.next

            #if temp is odd move the node to the beginning of list
            if temp.data % 2 != 0:
                prev_temp.next = x
                temp.next = head
                head = temp
            else:
                prev_temp = temp
            
            #advance temp pointer
            temp = x
        
        #Step 2:
        #split the list into odd and even
        temp = head.next
        prev_temp = head

        while temp != None and temp.data % 2 != 0 :
            prev_temp = temp
            temp = temp.next

        even = temp

        #end the odd list(make the last node)
        prev_temp.next = None

        #Step 3: 
        #merge even list into odd
        i = head
        j = even

        while i and j:
            #While both pointers are not exhausted, back up next pointers of i and j
            k = i.next
            l = j.next

            i.next = k
            j.next = l

            #ptr points to the latest node added
            ptr = j

            #advance i and j pointers
            i = k
            j = l

        if i == None:
            #odd list exhausts before even
            #append remainder of even list to odd
            ptr.next = j

        #The case where even list exhausts before odd list is automatically handled since we merge even list to the odd list
        return head




    def insertAfter(self, prev_node, new_data):
        """Steps to adding a node after a given node
            a. check if the given previous node exists
            b. create new_node and put in the data
            c. make next of new_node as next of prev_data
            d. make next of prev_node as new_node"""
        if prev_node is None: #check if the given previous node exists
            return
        new_node = Node(new_data) #create new_node and put in the data
        new_node.next = prev_node.next #make next of new_node as next of prev_data
        prev_node.next = new_node #make next of prev_node as new_node

    def append(self, new_data):
        """Steps to adding node at the end
            a. create a new_node and put in the data. Set next as None
            b. if the linkedlist is empty, make the new node as head
            c. else traverse till the last node
            d. change the next of last node"""
        new_node = Node(new_data) #create a new_node and put in the data. Set next as None
        if self.head is None: #if the linkedlist is empty, make the new node as head
            self.head = new_node
            return

        #else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node #change the next of last node

    def searchElement(self, k):
        """Iterative solution to searching nodes:
            a. Initialize node pointer, current = head
            b. Do following while current is not NULL
                - current->key being searched return True
                - current = current->next
            c. Return False"""
        current = self.head #initailize current to head
        while current: #loop until current not equal to none
            if current.data == k:
                return True #data found
            current = current.next
        return False #data not found


    #Function to reverse linked list
    def reverseList(self):
        """Iterative sol:
            a. Initialize three pointers prev as NULL, current as head, and next as NULL
            b. Iterate through the linked list. In loop do the following:
                - //Before changing next of current, store the next node
                    next = curr->next
                - //change next of current, this is where actual reversing happens
                    current->next = prev
                - //Move prev and current one step forward
                    prev = curr
                    curr = next"""
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    #counts the number of times a given int occurs
    def count(self, search_for):
        """Iteration method:
            1. Initialize count to 0
            2. Loop through each element of the linkedlist
                a. If element data is equal to the passed number then increament the count
            3. Return count"""
        current = self.head
        count = 0
        while current:
            if current.data == search_for:
                count += 1
            current = current.next
        return count



    #Function to get the middle of the linkedlist
    def printMiddle(self):
    # Initialize mid element as head and initialize a counter as 0. 
    # Traverse the list from head, while traversing increment the counter and change mid to mid->next whenever the counter is odd. 
    # So the mid will move only half of the total length of the list.  
        count = 0
        mid = self.head
        heads = self.head

        while heads:
            #update mid when count is odd
            if count & 1:
                mid = mid.next
            count += 1
            heads = heads.next
            #if empty list is provided
            if mid:
                print(f"The mid element is: ", mid.data)




    def deleteNode(self, key):
        """Iteratie method on steps to delete a node from the linked list:
            a. Find the previous node of the node to be deleted
            b. Change the next of the previous node
            c. Free memory of the previous node to be deleted"""

        #store head node
        temp = self.head

        #if head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                temp == temp.next
                temp = None
                return

        #search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #if key was not present in Linkedlist
        if (temp == None):
            return

        #unlink the node from the linked list
        prev.next = temp.next
        temp = None


    #Utility function to print the linkedlist
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, end = " ")
            temp = temp.next 

#code execution starts here
# if __name__ == "__main__":
llist = LinkedList()
llist.push(4)
llist.append(6)
llist.push(8)
llist.append(9)
llist.push(7)
llist.push(2)
llist.push(2)
llist.push(1)
llist.insertAfter(llist.head.next, 3)
print("Creation Linked List:")
llist.printList()
llist.printMiddle()
print(f"\n\nThe count of values is: ", llist.count(2))
llist.deleteNode(9)
print("\n\nLinked List after deletion of: 9")
#llist.printList()
llist.reverseList()
print(f"\n\nReversed linked list is: ")
llist.printList()


if llist.searchElement(24):
    print(f"\n\nYea")
else:
    print(f"\n\nNot Found")


