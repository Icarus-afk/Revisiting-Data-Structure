---
# Queues: A Comprehensive Study Guide

---

## 1. Overview

### What is a Queue?

A **queue** is a linear data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at one end (rear/back) and removed from the other end (front). Think of it like a line of people waiting - the person who arrived first is served first.

### Why This Version Exists

This implementation provides a foundational understanding of:
- Dynamic memory allocation (nodes created as needed)
- FIFO principle implementation
- Pointer/reference manipulation for both front and rear
- Constant time operations for core queue functions
- Trade-offs between simplicity and functionality

### When to Use It vs Alternatives

**Use Queues when:**
- You need FIFO access pattern (first item added is first item removed)
- Implementing breadth-first search algorithms
- Task scheduling systems
- Buffer for data streams
- Print job management
- Level-order tree traversal
- Simulating real-world queues (customers, requests, etc.)

**Use Stacks when:**
- You need LIFO access pattern (last in, first out)
- Implementing function call management
- Undo mechanisms in applications
- Expression evaluation and syntax parsing

**Use Arrays/Lists when:**
- You need random access by index
- You need flexible insertion/deletion positions
- You need to maintain insertion order with flexible access patterns

---

## 2. Node Structure

### Fields Explained

```python
class Node:
    def __init__(self, value):
        self.value = value  # The data stored in this node
        self.next = None    # Reference to the next node (or None if last)
```

**`value`**: The actual data payload. Can be any Python object (int, string, list, custom object, etc.)

**`next`**: A reference to the next Node object in the queue. When `None`, indicates this is the last node in the queue.

### Conceptual Diagram

```
Front of Queue                    Rear of Queue
┌─────┬────┐    ┌─────┬────┐    ┌─────┬────┐
│  1  │ ●──┼───→│  2  │ ●──┼───→│  3  │ None│
└─────┴────┘    └─────┴────┘    └─────┴────┘
 value  next     value  next     value  next
    ↑                                    ↑
  self.front                         self.rear
```

Each box represents a node. The queue has two pointers: front (for removals) and rear (for additions).

---

## 3. Full Implementation

### Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Queue Class

```python
class Queue:
    def __init__(self):
        self.front = None    # Points to the front element (to be dequeued next)
        self.rear = None     # Points to the rear element (last added)
        self.size = 0        # Keeps track of the number of elements in the queue

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        current = self.front
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return "Queue: " + " -> ".join(items)

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:           # Queue is empty
            self.front = new_node
            self.rear = new_node
        else:                           # Queue is not empty
            self.rear.next = new_node   # Link new node to rear
            self.rear = new_node        # Update rear to new node
        self.size += 1                  # Increment size

    def dequeue(self):
        if self.front is None:          # Queue is empty
            raise IndexError("Queue is empty")
        
        dequeue_value = self.front.value  # Store the value to return
        self.front = self.front.next      # Move front to next node
        
        if self.front is None:            # If queue becomes empty
            self.rear = None              # Reset rear to None too
        
        self.size -= 1                    # Decrement size
        return dequeue_value              # Return the dequeued value

    def peek(self):
        if self.front is None:          # Queue is empty
            raise IndexError("Queue is empty")
        return self.front.value         # Return the front value without removing it

    def is_empty(self):
        return self.front is None       # Check if front is None (empty queue)
```

---

## 4. Method-by-Method Breakdown

### `__init__(self)`

**Purpose**: Initialize an empty queue.

**Explanation**: Sets `self.front` and `self.rear` to `None`, indicating the queue is empty. Initializes `self.size` to 0 to keep track of the number of elements.

**Time Complexity**: O(1)

**Edge Cases**: None - always creates an empty queue.

---

### `__len__(self)`

**Purpose**: Return the number of elements in the queue.

**Step-by-Step**:
1. Simply return `self.size` which is maintained during enqueue/dequeue operations

**Time Complexity**: O(1) - constant time access to size

**Edge Cases Handled**:
- Empty queue (returns 0)

---

### `__repr__(self)`

**Purpose**: Return a string representation of the queue for printing.

**Step-by-Step**:
1. Initialize an empty list to collect values
2. Start at the front node
3. While current node exists:
   - Add string representation of current value to list
   - Move to next node
4. Join the values with " -> " and prefix with "Queue: "
5. Return the complete string

**Time Complexity**: O(n) - must visit every node

**Edge Cases Handled**:
- Empty queue (returns "Queue: ")

---

### `enqueue(self, value)`

**Purpose**: Add an element to the rear of the queue.

**Step-by-Step**:
1. Create a new node with the given value
2. Check if queue is empty (both front and rear are None)
3. If empty: set both front and rear to the new node
4. If not empty: link the current rear to the new node, then update rear to the new node
5. Increment the size counter

**Time Complexity**: O(1) - constant time operations

**Edge Cases Handled**:
- Empty queue (works correctly - new node becomes both front and rear)

**Visual Example**:
Before enqueue(4):
```
Front: [1] -> [2] -> [3] :Rear
```
After enqueue(4):
```
Front: [1] -> [2] -> [3] -> [4] :Rear
```

---

### `dequeue(self)`

**Purpose**: Remove and return the front element from the queue.

**Step-by-Step**:
1. Check if queue is empty - if so, raise IndexError
2. Store the value of the front node
3. Update the front pointer to the next node (removing the front node)
4. If the queue becomes empty (front is now None), also set rear to None
5. Decrement the size counter
6. Return the stored value

**Time Complexity**: O(1) - constant time operations

**Edge Cases Handled**:
- Empty queue (raises IndexError)
- Single-element queue (correctly sets both front and rear to None)

**Visual Example**:
Before dequeue():
```
Front: [1] -> [2] -> [3] :Rear
```
After dequeue():
```
Front: [2] -> [3] :Rear
Returns: 1
```

---

### `peek(self)`

**Purpose**: Return the front element without removing it.

**Step-by-Step**:
1. Check if queue is empty - if so, raise IndexError
2. Return the value of the front node without modifying the queue

**Time Complexity**: O(1) - constant time access to front

**Edge Cases Handled**:
- Empty queue (raises IndexError)

---

### `is_empty(self)`

**Purpose**: Check if the queue is empty.

**Step-by-Step**:
1. Return whether the front pointer is None

**Time Complexity**: O(1) - constant time comparison

**Edge Cases Handled**:
- Always works correctly (returns True if empty, False otherwise)

---

## 5. Time and Space Complexity Analysis

### Time Complexities:
- Enqueue: O(1) - constant time to add to rear
- Dequeue: O(1) - constant time to remove from front
- Peek: O(1) - constant time to access front
- is_empty: O(1) - constant time to check if empty
- len: O(1) - constant time to return size
- repr: O(n) - linear time to traverse all elements

### Space Complexity:
- Overall: O(n) where n is the number of elements in the queue
- Each operation: O(1) auxiliary space (no extra space needed beyond the node being added)

---

## 6. Common Use Cases and Applications

### Task Scheduling
- Operating systems use queues to manage processes
- Printer spooling systems
- CPU task scheduling

### Breadth-First Search
- Graph traversal algorithms
- Tree level-order traversal
- Finding shortest paths in unweighted graphs

### Simulation Systems
- Customer service simulations
- Traffic flow modeling

### Buffer Management
- Data buffering in streaming applications
- Keyboard input buffering
- Pipeline operations

---

## 7. Advantages and Disadvantages

### Advantages:
- Simple implementation with efficient operations
- O(1) time complexity for core operations (enqueue, dequeue, peek)
- Natural fit for FIFO problems
- Memory efficient for dynamic data sizes

### Disadvantages:
- No random access to elements (can only access front/rear)
- Searching takes O(n) time in worst case
- Extra memory overhead for pointers/references
- Cannot efficiently remove middle elements

---

## 8. Example Usage

```python
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Queue: 1 -> 2 -> 3
    print(queue.peek())  # 1
    print(queue.dequeue())  # 1
    print(queue)  # Queue: 2 -> 3
    print(len(queue))  # 2
    print(queue.is_empty())  # False
    queue.dequeue()
    queue.dequeue()
    print(queue.is_empty())  # True
```

This example demonstrates all core queue operations:
1. Creating a queue and enqueuing elements
2. Peeking at the front element
3. Dequeuing elements in FIFO order
4. Checking length and emptiness