# Linked Lists: A Comprehensive Study Guide

---

# Part 1: Singly Linked List

## 1. Overview

### What is a Singly Linked List?

A **singly linked list** is a linear data structure where each element (node) contains a value and a reference (pointer) to the next node in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations. Each node knows only about the next node, creating a one-way chain.

### Why This Version Exists

This implementation provides a foundational understanding of:
- Dynamic memory allocation (nodes created as needed)
- Pointer/reference manipulation
- Linear data structure traversal
- Trade-offs between access time and insertion flexibility

### When to Use It vs Alternatives

**Use Singly Linked Lists when:**
- You frequently insert/delete at the beginning (O(1) prepend)
- Memory is constrained (only one pointer per node)
- You only traverse in one direction
- You don't know the size in advance

**Use Arrays/Lists when:**
- You need random access by index (O(1) in arrays vs O(n) in linked lists)
- Memory locality matters for cache performance
- You primarily append and access elements

**Use Doubly Linked Lists when:**
- You need bidirectional traversal
- You frequently delete arbitrary nodes (if you have a reference to them)
- You need efficient operations at both ends

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

**`next`**: A reference to the next Node object in the chain. When `None`, indicates this is the last node.

### Conceptual Diagram

```
Node 1          Node 2          Node 3
┌─────┬────┐    ┌─────┬────┐    ┌─────┬────┐
│ 10  │ ●──┼───→│ 20  │ ●──┼───→│ 30  │ None│
└─────┴────┘    └─────┴────┘    └─────┴────┘
value  next     value  next     value  next
```

Each box represents a node. The `●` represents the `next` pointer, which points to the next node. The last node's `next` is `None`.

---

## 3. Full Implementation

### Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### SinglyLinkedList Class

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # O(n) linear time
    def __repr__(self):
        if self.head is None:
            return "→"
        else:
            last = self.head
            return_string = f"→ {last.value}"
            while last.next:
                last = last.next
                return_string += f" → {last.value}"
            return_string += " →"
            return return_string

    # O(n) linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(n) linear time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(1) constant time
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n) linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    # O(n) linear time
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n) linear time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                last.next = last.next.next

    # O(n) linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next  # BUG FIX: This line was missing!
            return last.value
```

### ⚠️ Bug Fix in `get` Method

**Original code** was missing `last = last.next` inside the loop, causing it to always return the head's value regardless of index.

**Why this matters**: Without advancing the pointer, the loop iterates but doesn't move through the list. The method would always return `self.head.value` for any valid index.

---

## 4. Method-by-Method Breakdown

### `__init__(self)`

**Purpose**: Initialize an empty linked list.

**Explanation**: Sets `self.head` to `None`, indicating the list is empty. The head pointer is the only entry point into the list.

**Time Complexity**: O(1)

**Edge Cases**: None - always creates an empty list.

---

### `__repr__(self)`

**Purpose**: Return a string representation of the list for printing.

**Step-by-Step**:
1. If list is empty (`self.head is None`), return just "→"
2. Start at the head node
3. Build a string starting with "→ {first_value}"
4. While there are more nodes (`last.next` exists):
   - Move to next node
   - Append " → {value}" to string
5. Add final "→" to indicate end
6. Return the complete string

**Time Complexity**: O(n) - must visit every node

**Edge Cases Handled**:
- Empty list (returns "→")

---

### `__contains__(self, value)`

**Purpose**: Enable the `in` operator (e.g., `5 in ll`).

**Step-by-Step**:
1. Start at head
2. While current node exists:
   - If current node's value matches target, return `True`
   - Move to next node
3. If we reach the end without finding it, return `False`

**Time Complexity**: O(n) - worst case checks all nodes

**Edge Cases Handled**:
- Empty list (loop never executes, returns `False`)
- Value at head
- Value at tail
- Value not present

---

### `__len__(self)`

**Purpose**: Enable `len(ll)` to get the number of nodes.

**Step-by-Step**:
1. Initialize counter to 0
2. Start at head
3. While current node exists:
   - Increment counter
   - Move to next node
4. Return counter

**Time Complexity**: O(n) - must count every node

**Edge Cases Handled**:
- Empty list (returns 0)

**Optimization Note**: Could maintain a size attribute for O(1) length checking, but this adds complexity to all insert/delete operations.

---

### `append(self, value)`

**Purpose**: Add a new node to the end of the list.

**Step-by-Step**:
1. If list is empty, create new node and set it as head
2. Otherwise:
   - Traverse to the last node (where `next` is `None`)
   - Create new node
   - Set last node's `next` to point to new node

**Time Complexity**: O(n) - must traverse to end

**Edge Cases Handled**:
- Empty list (special case)

**Optimization Note**: Maintaining a `tail` pointer would make this O(1), but your implementation doesn't do this (which is fine for learning purposes).

---

### `prepend(self, value)`

**Purpose**: Add a new node to the beginning of the list.

**Step-by-Step**:
1. Create new node
2. Set new node's `next` to current head
3. Update head to point to new node

**Time Complexity**: O(1) - no traversal needed!

**Edge Cases Handled**:
- Empty list (new node's `next` becomes `None`, which is correct)

**Why It's Fast**: We always have direct access to the head, so we can insert there instantly.

---

### `insert(self, value, index)`

**Purpose**: Insert a new node at a specific position.

**Step-by-Step**:
1. If index is 0, use `prepend()` (special case)
2. Otherwise:
   - Check if list is empty (error if so)
   - Traverse to node at position `index - 1`
   - If we run out of nodes before reaching `index - 1`, raise error
   - Create new node
   - Set new node's `next` to current node's `next`
   - Set current node's `next` to new node

**Time Complexity**: O(n) - worst case traverses to near end

**Edge Cases Handled**:
- Index 0 (delegates to `prepend`)
- Empty list (raises ValueError)
- Index out of bounds (raises ValueError)

**Visual Example**:
```
Before: → 10 → 20 → 30 →
insert(15, 1)

Step 1: Traverse to index 0 (value 10)
Step 2: Create new node with 15
Step 3: new_node.next = 10.next (points to 20)
Step 4: 10.next = new_node

After: → 10 → 15 → 20 → 30 →
```

---

### `delete(self, value)`

**Purpose**: Remove the first node with the specified value.

**Step-by-Step**:
1. If list is empty, do nothing
2. If head contains the value:
   - Update head to `head.next` (skip over first node)
3. Otherwise:
   - Traverse the list, checking `next` nodes
   - When `last.next.value` matches target:
     - Set `last.next = last.next.next` (bypass the node)
     - Break out of loop

**Time Complexity**: O(n) - may need to traverse entire list

**Edge Cases Handled**:
- Empty list (no operation)
- Value at head
- Value in middle
- Value at end

**Edge Cases NOT Handled**:
- Value not present (silently does nothing)

**Why Check `last.next`**: We need a reference to the node *before* the one we're deleting, so we can update its `next` pointer.

---

### `pop(self, index)`

**Purpose**: Remove the node at a specific index.

**Step-by-Step**:
1. If list is empty, raise error
2. Traverse to node at position `index - 1`
3. Verify that node at `index` exists (`last.next` is not `None`)
4. Set `last.next = last.next.next` (bypass the target node)

**Time Complexity**: O(n) - must traverse to index

**Edge Cases Handled**:
- Empty list (raises ValueError)
- Index out of bounds (raises ValueError)

**Edge Cases NOT Handled**:
- Index 0 (would fail - trying to access `last.next` when last is head)

**Bug Note**: This implementation can't pop index 0. A proper fix would add:
```python
if index == 0:
    self.head = self.head.next
```

---

### `get(self, index)`

**Purpose**: Retrieve the value at a specific index.

**Step-by-Step**:
1. If list is empty, raise error
2. Start at head
3. Traverse forward `index` times
4. If we run out of nodes, raise error
5. Return the value at that position

**Time Complexity**: O(n) - must traverse to index

**Edge Cases Handled**:
- Empty list (raises ValueError)
- Index out of bounds (raises ValueError)

**The Bug**: Original code was missing `last = last.next` in the loop. Without this, the loop counted to `index` but never moved the pointer, always returning the head value.

---

# Part 2: Doubly Linked List

## 1. Overview

### What is a Doubly Linked List?

A **doubly linked list** is a bidirectional linked data structure where each node contains:
- A value
- A pointer to the **next** node
- A pointer to the **previous** node

This allows traversal in both directions and more efficient operations when you have a reference to a specific node.

### Why This Version Exists

This implementation demonstrates:
- Bidirectional traversal capabilities
- More complex pointer management
- Trade-offs: more memory per node, but more flexibility
- How maintaining both head and tail pointers improves performance

### When to Use It vs Alternatives

**Use Doubly Linked Lists when:**
- You need efficient bidirectional traversal
- You frequently delete nodes when you have a reference to them
- You want O(1) append AND prepend operations (with tail pointer)
- You're implementing structures like LRU cache, deque, or browser history

**Use Singly Linked Lists when:**
- Memory is constrained (50% less pointer overhead)
- You only need forward traversal
- Simpler implementation is preferred

**Use Arrays/Lists when:**
- Random access is important
- Memory locality benefits outweigh insertion/deletion flexibility

---

## 2. Node Structure

### Fields Explained

```python
class Node:
    def __init__(self, value):
        self.value = value      # The data stored in this node
        self.next = None        # Reference to the next node
        self.previous = None    # Reference to the previous node
```

**`value`**: The data payload, same as singly linked list.

**`next`**: Reference to the next node in the forward direction.

**`previous`**: Reference to the previous node in the backward direction. The head's `previous` is `None`, indicating it's the first node.

### Conceptual Diagram

```
        Node 1              Node 2              Node 3
    ┌────┬─────┬────┐  ┌────┬─────┬────┐  ┌────┬─────┬────┐
    │None│ 10  │ ●──┼─→│ ●  │ 20  │ ●──┼─→│ ●  │ 30  │None│
    └────┴─────┴────┘  └─┼──┴─────┴────┘  └─┼──┴─────┴────┘
    prev value next       │    value next     │   value next
       ▲                  │                   │
       └──────────────────┘                   │
                    previous                  │
          ▲                                   │
          └───────────────────────────────────┘
                        previous
```

Each node maintains two pointers, allowing movement in both directions.

---

## 3. Full Implementation

### Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
```

### DoublyLinkedList Class

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) linear time
    def __repr__(self):
        if self.head is None:
            return "←"
        else:
            last = self.head
            return_string = f"← {last.value}"
            while last.next:
                last = last.next
                return_string += f" ↔ {last.value}"
            return_string += " →"
            return return_string

    # O(n) linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(1) constant time (thanks to tail pointer!)
    def append(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    # O(1) constant time
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        if self.head is not None:
            self.head.previous = first_node
        else:
            self.tail = first_node
        self.head = first_node

    # O(n) linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next

            new_node = Node(value)
            new_node.next = last.next
            new_node.previous = last
            if last.next is not None:
                last.next.previous = new_node
            else:
                self.tail = new_node
            last.next = new_node

    # O(n) linear time
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
                if self.head is not None:
                    self.head.previous = None
                else:
                    self.tail = None
            else:
                while last.next:
                    if last.next.value == value:
                        to_delete = last.next
                        last.next = to_delete.next
                        if to_delete.next is not None:
                            to_delete.next.previous = last
                        else:
                            self.tail = last
                        return
                    last = last.next

    # O(n) linear time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                to_delete = last.next
                last.next = to_delete.next
                if to_delete.next is not None:
                    to_delete.next.previous = last
                else:
                    self.tail = last

    # O(n) linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value
```

---

## 4. Method-by-Method Breakdown

### `__init__(self)`

**Purpose**: Initialize an empty doubly linked list.

**Explanation**: Sets both `self.head` and `self.tail` to `None`. Maintaining a tail pointer allows O(1) append operations.

**Time Complexity**: O(1)

**Edge Cases**: None

---

### `__repr__(self)`

**Purpose**: String representation for printing.

**Step-by-Step**: Nearly identical to singly linked list, but uses "↔" to show bidirectional connections and "←" for the start marker.

**Time Complexity**: O(n)

**Edge Cases Handled**: Empty list

---

### `__contains__(self, value)` & `__len__(self)`

These are identical to the singly linked list versions. Even though we have `previous` pointers, searching and counting still only move forward from head.

**Time Complexity**: O(n) for both

---

### `append(self, value)`

**Purpose**: Add a node to the end of the list.

**Step-by-Step**:
1. If list is empty:
   - Create new node
   - Set both head and tail to this node
2. Otherwise:
   - Create new node
   - Link current tail's `next` to new node
   - Link new node's `previous` to current tail
   - Update tail to new node

**Time Complexity**: O(1) - major improvement over singly linked list!

**Edge Cases Handled**:
- Empty list (both head and tail must be set)

**Why It's Fast**: The tail pointer gives us direct access to the last node, eliminating traversal.

**Visual Example**:
```
Before: ← 10 ↔ 20 →
        head   tail

append(30)

After: ← 10 ↔ 20 ↔ 30 →
       head       tail
```

---

### `prepend(self, value)`

**Purpose**: Add a node to the beginning.

**Step-by-Step**:
1. Create new node
2. Set new node's `next` to current head
3. If head exists:
   - Set head's `previous` to new node
4. Else (list was empty):
   - Set tail to new node
5. Update head to new node

**Time Complexity**: O(1)

**Edge Cases Handled**:
- Empty list (must set tail)
- Non-empty list (must update old head's `previous`)

**Key Difference from Singly**: Must maintain the bidirectional link by setting `head.previous`.

---

### `insert(self, value, index)`

**Purpose**: Insert at a specific position.

**Step-by-Step**:
1. If index 0, delegate to `prepend()`
2. Traverse to node at `index - 1`
3. Create new node
4. Set new node's `next` to current node's `next`
5. Set new node's `previous` to current node
6. If next node exists:
   - Update next node's `previous` to new node
7. Else (inserting at end):
   - Update tail to new node
8. Set current node's `next` to new node

**Time Complexity**: O(n)

**Edge Cases Handled**:
- Index 0
- Index out of bounds
- Inserting at end (must update tail)

**Critical Pointer Updates**: Four pointers must be updated correctly:
1. `new_node.next`
2. `new_node.previous`
3. `last.next`
4. `last.next.previous` (if it exists)

**Visual Example**:
```
Before: ← 10 ↔ 20 ↔ 30 →
insert(15, 1)

Step-by-step pointer updates:
1. new_node.next = 10.next (points to 20)
2. new_node.previous = 10
3. 20.previous = new_node
4. 10.next = new_node

After: ← 10 ↔ 15 ↔ 20 ↔ 30 →
```

---

### `delete(self, value)`

**Purpose**: Remove first node with specified value.

**Step-by-Step**:
1. If list is empty, do nothing
2. If head contains value:
   - Update head to `head.next`
   - If new head exists, set its `previous` to `None`
   - Else (list now empty), set tail to `None`
3. Otherwise:
   - Traverse looking at `next` nodes
   - When found:
     - Store reference to node being deleted
     - Update `last.next` to skip deleted node
     - If deleted node has a next:
       - Update that next node's `previous` to `last`
     - Else (deleted tail):
       - Update tail to `last`
     - Return

**Time Complexity**: O(n)

**Edge Cases Handled**:
- Empty list
- Delete head (must update head.previous)
- Delete tail (must update tail pointer)
- Delete middle node
- Value not present (no-op)

**Pointer Count**: Up to 4 pointers must be updated when deleting a middle node.

---

### `pop(self, index)`

**Purpose**: Remove node at specific index.

**Step-by-Step**:
1. Check if list is empty (error)
2. Traverse to node at `index - 1`
3. Verify node at `index` exists
4. Store reference to node being deleted
5. Update `last.next` to skip deleted node
6. If deleted node has a next:
   - Update next node's `previous` to `last`
7. Else:
   - Update tail to `last`

**Time Complexity**: O(n)

**Edge Cases Handled**:
- Empty list
- Index out of bounds
- Popping tail (must update tail pointer)

**Edge Cases NOT Handled**:
- Index 0 (same bug as singly linked list)

---

### `get(self, index)`

**Purpose**: Retrieve value at index.

**Implementation**: Identical to singly linked list (traverses forward).

**Time Complexity**: O(n)

**Potential Optimization**: Could traverse from tail backward if `index > len/2`, reducing average case to O(n/2). Your implementation doesn't do this, which is fine.

---

## 5. Comparison Section

### Singly vs Doubly Linked List

| Aspect | Singly Linked | Doubly Linked |
|--------|---------------|---------------|
| **Memory per node** | 2 fields (value, next) | 3 fields (value, next, previous) |
| **Traversal** | Forward only | Both directions |
| **Append complexity** | O(n) without tail, O(1) with tail | O(1) with tail pointer |
| **Prepend complexity** | O(1) | O(1) |
| **Delete given node** | O(n) - need reference to previous | O(1) - if you have reference to node itself |
| **Implementation complexity** | Simpler | More complex pointer management |
| **Space overhead** | ~50% less | ~50% more |

### Memory Trade-offs

**Singly Linked List**:
- Each node: ~28 bytes (8 bytes value ref + 8 bytes next + 12 bytes Python overhead)
- 1000 nodes: ~28 KB

**Doubly Linked List**:
- Each node: ~36 bytes (8 bytes value ref + 8 bytes next + 8 bytes previous + 12 bytes overhead)
- 1000 nodes: ~36 KB

**Conclusion**: Doubly linked lists use approximately 30% more memory for the node structure itself.

### Performance Differences

**Both Implementations**:
- Search: O(n)
- Access by index: O(n)
- Insert at index: O(n)

**Singly Linked (your implementation)**:
- Append: O(n) - no tail pointer
- Prepend: O(1)

**Doubly Linked (your implementation)**:
- Append: O(1) - has tail pointer
- Prepend: O(1)

**Key Advantage of Doubly**: If you have a reference to a specific node, you can delete it in O(1) time because you can access its previous node directly.

### Real-world Use Cases

**Singly Linked Lists**:
- Implementation of stacks (only need to access top)
- Simple job queues
- Hash table collision chains (when simple is better)
- Undo functionality (forward-only history)

**Doubly Linked Lists**:
- Browser history (forward and back buttons)
- LRU (Least Recently Used) cache implementation
- Music player (previous/next track)
- Text editors (cursor movement)
- Deque (double-ended queue) implementation
- Implementing undo/redo with bidirectional traversal

---

## 6. Common Pitfalls

### 1. Forgetting to Update Head/Tail Pointers

**Problem**: When inserting or deleting at the boundaries (first or last node), failing to update head or tail pointers.

**Example Bug**:
```python
# Deleting the only node in list
self.head = None
# Forgot: self.tail = None
# Now tail points to deleted node!
```

**Solution**: Always check if you're modifying head or tail and update both.

---

### 2. Breaking the Bidirectional Link (Doubly)

**Problem**: In doubly linked lists, updating `next` without updating corresponding `previous`, or vice versa.

**Example Bug**:
```python
# Inserting between nodes
new_node.next = current.next
current.next = new_node
# Forgot: new_node.previous = current
# Forgot: if new_node.next: new_node.next.previous = new_node
# Now the backward chain is broken!
```

**Solution**: For every link you create, create its counterpart. Think in pairs: `A.next = B` requires `B.previous = A`.

---

### 3. Null Pointer Dereferencing

**Problem**: Attempting to access `.next` or `.previous` on `None`.

**Example Bug**:
```python
current = self.head
current = current.next  # What if head is None?
value = current.value   # Crash!
```

**Solution**: Always check `if node is not None` before accessing its attributes.

---

### 4. Off-by-One Errors in Traversal

**Problem**: Traversing to the wrong position, especially when needing the node *before* the target.

**Example**: When inserting at index 2, you need to traverse to index 1 (the node before), not index 2.

**Solution**: Draw diagrams. Remember: to insert/delete at index `i`, you often need to be at index `i-1`.

---

### 5. Forgetting Edge Cases

**Critical edge cases to test**:
- Empty list
- Single-element list
- Operation at head (index 0)
- Operation at tail (last index)
- Value not present (for delete/search)
- Index out of bounds

**Example Bug in Your Code**: The `pop(index)` method doesn't handle index 0.

---

### 6. Memory Leaks (In Languages with Manual Memory Management)

**Python handles this automatically**, but in C/C++, you must `delete` or `free` removed nodes.

**Why it matters for understanding**: Even though Python has garbage collection, understanding that deleted nodes should be fully disconnected helps you avoid logical errors where removed nodes are still reachable.

---

### 7. Modifying List While Iterating

**Problem**:
```python
last = self.head
while last:
    if some_condition:
        self.delete(last.value)  # Modifying during iteration!
    last = last.next
```

**Why it breaks**: Deleting might change pointers you're about to use.

**Solution**: Collect nodes to delete, then delete them after iteration, or use careful pointer manipulation.

---

## 7. Practice Exercises

### Exercise 1: Reverse a Singly Linked List (Easy)

Implement a method `reverse()` that reverses the singly linked list in-place.

**Example**:
```python
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)  # → 1 → 2 → 3 →
ll.reverse()
print(ll)  # → 3 → 2 → 1 →
```

**Hints**:
- You need to reverse all `next` pointers
- Think about three pointers: previous, current, next
- Don't forget to update `self.head`

---

### Exercise 2: Find Middle Element (Medium)

Implement a method `find_middle()` that returns the value of the middle node. If the list has an even number of nodes, return the second middle node.

**Example**:
```python
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print(ll.find_middle())  # 3

ll.append(6)
print(ll.find_middle())  # 4 (second middle)
```

**Hints**:
- Try to solve this in one pass (without using `__len__`)
- Use two pointers: one slow (moves 1 step), one fast (moves 2 steps)
- When fast reaches the end, slow is at the middle

---

### Exercise 3: Detect Cycle (Medium-Hard)

Implement a method `has_cycle()` that returns `True` if the list contains a cycle (a node's `next` eventually points back to a previous node), `False` otherwise.

**Example**:
```python
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.has_cycle())  # False

# Create a cycle manually (for testing)
ll.tail.next = ll.head.next  # 3 -> 2, creating: 1 -> 2 -> 3 -> 2 -> ...
print(ll.has_cycle())  # True
```

**Hints**:
- Floyd's Cycle Detection Algorithm (tortoise and hare)
- Two pointers at different speeds
- If they ever meet, there's a cycle
- If fast reaches `None`, there's no cycle

---

### Exercise 4: Merge Two Sorted Lists (Hard)

Write a function that takes two sorted singly linked lists and returns a new sorted list containing all elements from both.

**Example**:
```python
ll1 = SinglyLinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = SinglyLinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

result = merge_sorted_lists(ll1, ll2)
print(result)  # → 1 → 2 → 3 → 4 → 5 → 6 →
```

**Hints**:
- Create a new list
- Compare values at current positions in both lists
- Append the smaller value
- Move forward in the list you took from
- Handle remaining elements when one list is exhausted

---

### Exercise 5: Debug the Issue (Debugging)

The following code is supposed to remove all duplicate values from a doubly linked list, but it has bugs. Find and fix them.

```python
def remove_duplicates(self):
    """Remove duplicate values from the doubly linked list"""
    if self.head is None:
        return
    
    seen = set()
    current = self.head
    
    while current:
        if current.value in seen:
            # Remove this node
            current.previous.next = current.next
            current.next.previous = current.previous
        else:
            seen.add(current.value)
        current = current.next
```

**Test case**:
```python
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(1)
dll.append(3)
dll.append(2)
dll.remove_duplicates()
print(dll)  # Should be: ← 1 ↔ 2 ↔ 3 →
```

**Questions**:
1. What happens when the first node is a duplicate?
2. What happens when the last node is a duplicate?
3. What other edge cases might cause crashes?

**Hints**:
- Think about `None` pointer access
- What if head is a duplicate?
- What if tail is a duplicate?
- Consider the state of `previous` and `next` at boundaries

---

## Summary

You've now studied two fundamental data structures with practical implementations. Key takeaways:

1. **Linked lists trade random access for insertion flexibility**
2. **Pointer management is the core skill** - every operation is about carefully updating references
3. **Edge cases matter** - empty lists, single elements, and boundary operations require special handling
4. **Doubly linked lists offer more features at the cost of complexity and memory**
5. **Time complexity analysis helps you choose the right data structure**

Keep practicing pointer manipulation, draw diagrams for complex operations, and always test edge cases. These skills transfer directly to trees, graphs, and other advanced data structures.

---

**Next Steps**:
- Implement the practice exercises
- Try implementing a circular linked list
- Study how `collections.deque` is implemented in Python
- Learn about XOR linked lists (memory-efficient doubly linked lists)
- Explore how linked lists are used in operating system memory management
