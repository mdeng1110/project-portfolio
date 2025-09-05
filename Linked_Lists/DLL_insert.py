class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoubleLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next_node

    def get_size_list(self):
        count = 0
        curr_node = self.head
        while curr_node != None:
            count = count + 1
            curr_node = curr_node.next_node
        return count
    
    def insert_beg(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        new_node.prev_node = None
        if self.head != None:
            self.head.prev_node = new_node
        self.head = new_node

double_list = DoubleLinkedList()
#insert values
double_list.insert_beg(90)
double_list.insert_beg(90)
double_list.insert_beg(90)
double_list.insert_beg(80)
double_list.insert_beg(70)
#traverse the list
print('-'*100)
print('After Insertion')
print('-'*100)
double_list.traverse()
print('Length')
print(double_list.get_size_list())
