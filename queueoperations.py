class Queue:
    def __init__(self):
        self.items = []

    # Enqueue operation
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue operation
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")
            return None

    # Peek operation
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty.")
            return None

    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display queue
    def display(self):
        print("Queue:", self.items)

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()      # Queue: [10, 20, 30]
print(queue.dequeue())  # 10
queue.display()      # Queue: [20, 30]
print(queue.peek())  # 20