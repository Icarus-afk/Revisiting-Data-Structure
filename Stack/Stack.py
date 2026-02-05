class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    # O(1) constant time
    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return "Stack: " + " -> ".join(items)
    
    # O(1) constant time
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1             
        
    # O(1) constant time    
    def pop (self):
        if self.top is None:
            raise ValueError("Stack is empty")
        pop_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return pop_value

    # O(1) constant time
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value
    
    def is_empty(self):
        return self.top is None
    
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)  # Stack: 3 -> 2 -> 1
    print(stack.peek())  # 3
    print(stack.pop())   # 3
    print(stack)  # Stack: 2 -> 1
    print(len(stack))  # 2
    print(stack.is_empty())  # False
    stack.pop()
    stack.pop()
    print(stack.is_empty())  # True
    