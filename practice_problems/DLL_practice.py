class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # keep track of the tail for easier appending

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # empty list
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ↔ ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ↔ ")
            current = current.prev
        print("None")

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current  
            current = current.next
        return None  

    def delete(self, value):
        current = self.head

        while current:
            if current.data == value:
                # Case 1: Node is the head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                # Case 2: Node is the tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Case 3: Node is in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True  # Deletion successful
            current = current.next

        return False  # Value not found
    
    def reverse(self):
        current = self.head
        prev_node = None

        while current:
            # Swap next and prev pointers
            current.prev, current.next = current.next, current.prev
            
            # Move prev_node to current before shifting
            prev_node = current

            # Move to the next node in the *original* direction
            current = current.prev

        # After loop, prev_node will be the new head
        if prev_node:
            self.head = prev_node

    def partition_list(self, x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        
        while current:
            if current.data < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next
            
            prev1.next = dummy2.next
            if dummy2.next:
                dummy2.next.prev = prev1
            
            prev2.next = None
            
            self.head = dummy1.next
            self.head.prev = None

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

# if __name__ == "__main__":
    # dll = DoublyLinkedList()
    
    # Append nodes
    # dll.append(10)
    # dll.append(20)
    # dll.append(30)
    # dll.append(40)
    # print("Forward traversal after append:")
    # dll.display_forward()
    
    # # Prepend node
    # dll.prepend(5)
    # print("\nForward traversal after prepend:")
    # dll.display_forward()
    
    # print("\nBackward traversal:")
    # dll.display_backward()
    
    # print("\nSearch:")
    # DLL_node = dll.search(30)
    # print(DLL_node.data)

    # print("\nDeleting 10 (head):")
    # dll.delete(10)
    # dll.display_forward()

    # print("\nDeleting 30 (middle):")
    # dll.delete(30)
    # dll.display_forward()

    # print("\nDeleting 40 (tail):")
    # dll.delete(40)
    # dll.display_forward()

# dll = DoublyLinkedList()
# dll.append(10)
# dll.append(20)
# dll.append(30)
# dll.append(40)

# print("Original:")
# dll.display_forward()

# dll.reverse()

# print("\nReversed:")
# dll.display_forward()


    
# -------------------------------
# Test Cases:
# -------------------------------

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList()
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.display_forward()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.display_forward()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList()
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.display_forward()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.display_forward()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList()
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.display_forward()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.display_forward()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList()
dll4.make_empty()
print("BEFORE: ", end="")
dll4.display_forward()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.display_forward()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList()
print("BEFORE: ", end="")
dll5.display_forward()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.display_forward()