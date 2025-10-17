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

    def search(self, value):
        """Return True if the value is found, else False."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

if __name__ == "__main__":
    ll = LinkedList()

    # Append elements
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("After appending:")
    ll.display()

    # Prepend element
    # ll.prepend(5)
    # print("\nAfter prepending:")
    # ll.display()

    # Delete element
    # ll.delete(20)
    # print("\nAfter deleting 20:")
    # ll.display()

    print("\nSearch for 20:", ll.search(20))  # True
    print("Search for 50:", ll.search(50))    # False

