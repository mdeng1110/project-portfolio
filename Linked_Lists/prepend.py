class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def empty(self):
        return self.length == 0


    def prepend(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.length += 1
            return 
        new_node.next = self.head
        self.head = new_node
        self.length += 1


    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> " if current.next else " ")
            current = current.next
        print()

my_list = LinkedList()
my_list.prepend(30)
my_list.prepend(20)
my_list.prepend(10)

my_list.display()