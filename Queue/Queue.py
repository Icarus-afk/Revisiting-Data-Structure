class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # O(1) constant time
    def __len__(self):
        return self.size

    # O(n) linear time
    def __repr__(self):
        items = []
        current = self.front
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return "Queue: " + " -> ".join(items)

    # O(1) constant time
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    # O(1) constant time
    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty")

        dequeue_value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return dequeue_value

    # O(1) constant time
    def peek(self):
        if self.front is None:
            raise IndexError("Queue is empty")
        return self.front.value

    # O(1) constant time
    def is_empty(self):
        return self.front is None


if __name__ == "__main__":
    queue = Stack()
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
