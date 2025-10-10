class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    # Display list
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")

# Example usage
cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.display()  # 10 -> 20 -> 30 -> (head)