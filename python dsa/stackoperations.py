class Stack:
    def __init__(self):
        self.items = []

    # Push operation
    def push(self, item):
        self.items.append(item)

    # Pop operation
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")
            return None

    # Peek operation
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty.")
            return None

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display stack
    def display(self):
        print("Stack:", self.items)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()      # Stack: [10, 20, 30]
print(stack.pop())   # 30
stack.display()      # Stack: [10, 20]
print(stack.peek())  # 20