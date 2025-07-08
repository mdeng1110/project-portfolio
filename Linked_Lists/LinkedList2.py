class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = node(data)
            return
         
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.head.next = cur.next

    def length(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.display()