class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    # Insert at position (0-based index)
    def insert_position(self, data, pos):
        if pos == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if curr is None:
                return
            curr = curr.next
        if curr is None:
            return
        new_node.next = curr.next
        curr.next = new_node

    # Delete from beginning
    def delete_beginning(self):
        if self.head:
            self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    # Delete from position (0-based index)
    def delete_position(self, pos):
        if pos == 0 and self.head:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(pos - 1):
            if curr is None or curr.next is None:
                return
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    # Search for a value
    def search(self, value):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == value:
                return pos
            curr = curr.next
            pos += 1
        return -1

    # Update value at position
    def update(self, pos, new_data):
        curr = self.head
        for _ in range(pos):
            if curr is None:
                return
            curr = curr.next
        if curr:
            curr.data = new_data

    # Count length
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # Display list
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_beginning(5)
sll.insert_position(15, 2)
sll.display()  # 5 -> 10 -> 15 -> 20 -> None

sll.delete_beginning()
sll.display()  # 10 -> 15 -> 20 -> None

sll.delete_end()
sll.display()  # 10 -> 15 -> None

sll.delete_position(1)
sll.display()  # 10 -> None

print("Length:", sll.length())  # Length: 1

sll.insert_end(25)
sll.insert_end(30)
sll.display()  # 10 -> 25 -> 30 -> None

print("Search for 25:", sll.search(25))  # Search for 25: 1

sll.update(1, 26)
sll.display()  # 10 -> 26 -> 30 -> None