class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a new node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node with matching data"""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):
        """Print the list contents"""
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
