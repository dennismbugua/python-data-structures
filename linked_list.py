class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node data: {self.data}"

class LinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head == None

    def size(self):
        """Returns the number of Nodes and takes linear time 0(n)"""
        current = self.head
        count = 0

        #while current: is the same as while current != None
        while current != None:
            count = count + 1
            current = current.next_node

        return count

    def add(self, data):
        """Adds new node containing data at the head of the list. Takes linear time 0(n)"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Searches for the first node containing data that matches the key
        Returns the node or 'None' if not found

        Takes 0(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes constant time 0(1)
        find the node at the insertion point takes linear time

        Takes an overal linear time
        """
        if index == 0:
            self.add(data)
        if index > 1:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or None of key doesn't exist
        Takes linear time 0(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def __repr__(self):
        nodes = []
        current = self.head
        while current != None:
            if current is self.head:
                nodes.append(f"Head is: {current.data}")
            elif current.next_node is None:
                nodes.append(f"Tail is: {current.data}")
            else:
                nodes.append(f"{current.data}")

            current = current.next_node
        
        return '-> '.join(nodes)

