from node import Node

# Class to create a Doubly Linked List
class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node


    # Given a reference to the head of DLL and integer,
    # appends a new node at the end
    def append(self, new_data):

        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(new_data)

        # 3. This new node is going to be the last node,
        # so make next of it as None
        new_node.next = None

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while(last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last

        return

    # replaces the element at the given position with the given element
    def replace(self, pos, new_data):
        current = self.head
        while pos > 0:
            current = current.next
            pos -= 1
            if current.next is None:
                print("invalid pos")
                return
        current.data = new_data

    # returns the element at the given position
    def get(self, pos):
        current = self.head
        while pos > 0:
            current = current.next
            pos -= 1
            if current is None:
                #print("invalid pos")
                return
        return current.data


    # This function prints contents of linked list
    # starting from the given node
    def printList(self, node):
        while(node is not None):
            print (" %s" % (node.data))
            last = node
            node = node.next

        #print("\nTraversal in reverse direction")
        #while(last is not None):
        #    print (" %s" % (last.data))
        #    last = last.prev

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
