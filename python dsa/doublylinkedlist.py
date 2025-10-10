class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Delete from beginning
    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    # Delete from end
    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    # Display list forward
    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            last = curr
            curr = curr.next
        print("None")

    # Display list backward
    def display_backward(self):
        curr = self.head
        if not curr:
            print("None")
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_beginning(5)
dll.display_forward()    # 5 <-> 10 <-> 20 <-> None
dll.display_backward()   # 20 <-> 10 <-> 5 <-> None
dll.delete_beginning()
dll.display_forward()    # 10 <-> 20 <-> None
dll.delete_end()
dll.display_forward()    # 10 <-> None