class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    # Display list forward
    def display_forward(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while True:
            print(curr.data, end=" <-> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")

    # Display list backward
    def display_backward(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head.prev
        while True:
            print(curr.data, end=" <-> ")
            curr = curr.prev
            if curr == self.head.prev:
                break
        print("(head)")

# Example usage
cdll = CircularDoublyLinkedList()
cdll.insert_end(10)
cdll.insert_end(20)
cdll.insert_end(30)
cdll.display_forward()    # 10 <-> 20 <-> 30 <-> (head)
cdll.display_backward()   # 30 <-> 20 <-> 10 <-> (head)