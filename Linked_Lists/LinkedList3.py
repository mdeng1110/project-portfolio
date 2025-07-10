class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        if self.empty():
            self.head = Node(value)
            self.length += 1
        return
            
        new_node = Node(value)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.head.next = cur.next
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def empty(self):
        return self.length == 0
    
    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

my_linked_list = Linked_List()
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.display()

        