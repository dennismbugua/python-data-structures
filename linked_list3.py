class Node:
    #constructor initializing the object of the node
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    #constructor initailizing the object of the linkedlist/head
    def __init__(self):
        self.head = None

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




    #Reverse linkedlist in groups of a given size
    def reverse(self, head, k):
        """
        1.  Reverse the first sub-list of size k. While reversing keep track of the next node and previous node. 
            Let the pointer to the next node be next and pointer to the previous node be prev. 
        2.  head->next = reverse(next, k) ( Recursively call for rest of the list and link the two sub-lists )
        3.  Return prev 
        """
        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        #Reverse first k nodes of the linkedlist
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        
        #Next is now a pointer to (k+1)th node
        #Recursively call for the list starting from current
        #And make the rest of the list as next of first node
        if next is not None:
            head.next = self.reverse(next, k)

        #prev is the new head of the input list
        return prev


    #inserting a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNodeAtGivenPosition(self, post):
        #if linkedlist is empty
        if self.head is None:
            return

        #store head node
        temp = self.head

        #if head needs to be removed
        if post == 0:
            temp = temp.next
            temp == None
            return

        #find the previous node of the node to be deleted
        for i in range(post -1):
            temp = temp.next
            if temp is None:
                break

        #if position is more than the number of nodes
        if temp is None:
            return 
        if temp.next is None:
            return

        #Node temp.next is the node to be deleted
        #store pointer to the next of the node to be deleted
        next = temp.next.next

        #unlink the node from the linkedlist
        temp.next = None
        temp.next = next

    #Utility function to print the linkedlist
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, end = " ")
            temp = temp.next 

if __name__ == "__main__":
    llist = linkedList()
    llist.push(2)
    llist.push(4)
    llist.push(8)
    llist.push(9)
    llist.push(10)
    llist.push(21)
    print(f"Created LinkedList")
    llist.printList()
    llist.head = llist.reverse(llist.head, 3)
    print(f"\n\nReversed linked list")
    llist.printList()
    llist.deleteNodeAtGivenPosition(3)
    print("\n\nLinkedList after deletion of position: 3")
    llist.printList()