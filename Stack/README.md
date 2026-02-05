---
# Stacks: A Comprehensive Study Guide

---

## 1. Overview

### What is a Stack?

A **stack** is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Elements are added and removed from the same end, called the "top" of the stack. Think of it like a stack of plates - you can only add or remove plates from the top.

### Why This Version Exists

This implementation provides a foundational understanding of:
- Dynamic memory allocation (nodes created as needed)
- LIFO principle implementation
- Pointer/reference manipulation
- Constant time operations for core stack functions
- Trade-offs between simplicity and functionality

### When to Use It vs Alternatives

**Use Stacks when:**
- You need LIFO access pattern (last item added is first item removed)
- Implementing function call management (call stack)
- Undo mechanisms in applications
- Expression evaluation and syntax parsing
- Backtracking algorithms
- Browser history (back button functionality)

**Use Queues when:**
- You need FIFO access pattern (first in, first out)
- Processing items in the order they arrive
- Breadth-first search algorithms

**Use Arrays/Lists when:**
- You need random access by index
- You need to access elements from both ends
- You need to maintain insertion order with flexible access patterns

---

## 2. Node Structure

### Fields Explained

```python
class Node:
    def __init__(self, value):
        self.value = value  # The data stored in this node
        self.next = None    # Reference to the next node (or None if bottom of stack)
```

**`value`**: The actual data payload. Can be any Python object (int, string, list, custom object, etc.)

**`next`**: A reference to the next Node object in the stack. When `None`, indicates this is the bottom node of the stack.

### Conceptual Diagram

```
Top of Stack
┌─────┬────┐
│  3  │ ●──┼───→ (points to next node)
└─────┴────┘
 value  next
    ↑
  self.top

┌─────┬────┐
│  2  │ ●──┼───→ (points to next node)
└─────┴────┘
 value  next

┌─────┬────┐
│  1  │ None│ ← Bottom of Stack
└─────┴────┘
 value  next
```

Each box represents a node. The stack grows downward, with the most recently added item at the top.

---

## 3. Full Implementation

### Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Stack Class

```python
class Stack:
    def __init__(self):
        self.top = None      # Points to the topmost element in the stack
        self.size = 0        # Keeps track of the number of elements in the stack

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
        new_node.next = self.top      # New node points to previous top
        self.top = new_node           # Update top to new node
        self.size += 1                # Increment size

    # O(1) constant time
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")  # Cannot pop from empty stack
        pop_value = self.top.value    # Store the value to return
        self.top = self.top.next      # Move top to the next node
        self.size -= 1                # Decrement size
        return pop_value              # Return the popped value

    # O(1) constant time
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")  # Cannot peek at empty stack
        return self.top.value         # Return the top value without removing it

    def is_empty(self):
        return self.top is None       # Check if top is None (empty stack)
```

---

## 4. Method-by-Method Breakdown

### `__init__(self)`

**Purpose**: Initialize an empty stack.

**Explanation**: Sets `self.top` to `None`, indicating the stack is empty. Initializes `self.size` to 0 to keep track of the number of elements.

**Time Complexity**: O(1)

**Edge Cases**: None - always creates an empty stack.

---

### `__len__(self)`

**Purpose**: Return the number of elements in the stack.

**Step-by-Step**:
1. Simply return `self.size` which is maintained during push/pop operations

**Time Complexity**: O(1) - constant time access to size

**Edge Cases Handled**:
- Empty stack (returns 0)

---

### `__repr__(self)`

**Purpose**: Return a string representation of the stack for printing.

**Step-by-Step**:
1. Initialize an empty list to collect values
2. Start at the top node
3. While current node exists:
   - Add string representation of current value to list
   - Move to next node
4. Join the values with " -> " and prefix with "Stack: "
5. Return the complete string

**Time Complexity**: O(n) - must visit every node

**Edge Cases Handled**:
- Empty stack (returns "Stack: ")

---

### `push(self, value)`

**Purpose**: Add an element to the top of the stack.

**Step-by-Step**:
1. Create a new node with the given value
2. Set the new node's `next` to point to the current top
3. Update the stack's `top` to point to the new node
4. Increment the size counter

**Time Complexity**: O(1) - constant time operations

**Edge Cases Handled**:
- Empty stack (works correctly - new node becomes top and bottom)

**Visual Example**:
Before push(4):
```
Top: [3] -> [2] -> [1] -> None
```
After push(4):
```
Top: [4] -> [3] -> [2] -> [1] -> None
```

---

### `pop(self)`

**Purpose**: Remove and return the top element from the stack.

**Step-by-Step**:
1. Check if stack is empty - if so, raise ValueError
2. Store the value of the top node
3. Update the top pointer to the next node (removing the top node)
4. Decrement the size counter
5. Return the stored value

**Time Complexity**: O(1) - constant time operations

**Edge Cases Handled**:
- Empty stack (raises ValueError)
- Single-element stack (correctly sets top to None)

**Visual Example**:
Before pop():
```
Top: [4] -> [3] -> [2] -> [1] -> None
```
After pop():
```
Top: [3] -> [2] -> [1] -> None
Returns: 4
```

---

### `peek(self)`

**Purpose**: Return the top element without removing it.

**Step-by-Step**:
1. Check if stack is empty - if so, raise ValueError
2. Return the value of the top node without modifying the stack

**Time Complexity**: O(1) - constant time access to top

**Edge Cases Handled**:
- Empty stack (raises ValueError)

---

### `is_empty(self)`

**Purpose**: Check if the stack is empty.

**Step-by-Step**:
1. Return whether the top pointer is None

**Time Complexity**: O(1) - constant time comparison

**Edge Cases Handled**:
- Always works correctly (returns True if empty, False otherwise)

---

## 5. Time and Space Complexity Analysis

### Time Complexities:
- Push: O(1) - constant time to add to top
- Pop: O(1) - constant time to remove from top
- Peek: O(1) - constant time to access top
- is_empty: O(1) - constant time to check if empty
- len: O(1) - constant time to return size
- repr: O(n) - linear time to traverse all elements

### Space Complexity:
- Overall: O(n) where n is the number of elements in the stack
- Each operation: O(1) auxiliary space (no extra space needed beyond the node being added)

---

## 6. Common Use Cases and Applications

### Function Call Management
- Programming languages use call stacks to manage function calls
- Each function call is pushed onto the stack, popped when returning

### Expression Evaluation
- Evaluating postfix expressions
- Converting infix to postfix/prefix notation
- Parentheses matching in compilers

### Undo Operations
- Text editors use stacks to implement undo functionality
- Each action is pushed, undo pops the last action

### Backtracking Algorithms
- Depth-first search in graphs
- Maze solving algorithms
- Tree traversals (iterative implementations)

---

## 7. Advantages and Disadvantages

### Advantages:
- Simple implementation with efficient operations
- O(1) time complexity for core operations (push, pop, peek)
- Memory efficient for dynamic data sizes
- Natural fit for LIFO problems

### Disadvantages:
- No random access to elements (can only access top)
- Searching takes O(n) time in worst case
- Extra memory overhead for pointers/references
- Potential for stack overflow with deep recursion

---

## 8. Example Usage

```python
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
```

This example demonstrates all core stack operations:
1. Creating a stack and pushing elements
2. Peeking at the top element
3. Popping elements in LIFO order
4. Checking length and emptiness