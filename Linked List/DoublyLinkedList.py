class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


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

    # O(n) linear time
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


if __name__ == "__main__":
    ll = DoublyLinkedList()

    ll.append(10)
    ll.insert(5, 1)
    ll.insert(15, 1)
    ll.insert(18, 1)
    ll.insert(22, 1)
    ll.insert(29, 1)

    print(ll)

    ll.prepend(100)

    print(ll)

    ll.insert(200, 1)

    print(ll)

    ll.delete(18)
    ll.delete(100)
    ll.delete(29)

    print(ll)

    ll.pop(1)

    print(ll)

    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)
