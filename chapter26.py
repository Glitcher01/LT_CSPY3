from chapter24 import Node
import time


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

    def is_empty(self):
        return self.length == 0


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


class ListQueue:
    def __init__(self):
        self.queue = []
        self.length = 0
        self.head = None

    def insert(self, cargo):
        self.queue.append(cargo)
        self.head = self.queue[0]

    def remove(self):
        cargo = self.queue.pop()
        self.head = None if len(self.queue) == 0 else self.queue[0]
        return cargo

    def is_empty(self):
        return len(self.queue) is 0

    def __str__(self):
        return str(self.queue)


class Linked_Priority:
    def __init__(self):
        self.head = None
        self.length = 0
        self.last = None
        self.list = []

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
            self.length += 1
        else:
            item = self.head
            if cargo >= item.cargo:
                self.head = node
                self.head.next = item
                self.length += 1
                return
            while item.next is not None:
                if cargo >= item.next.cargo:
                    node.next = item.next
                    item.next = node
                    self.length += 1
                    return
                item = item.next
            self.last.next = node
            self.last = node
            self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length is 0:
            self.last = None
        return cargo

    def is_empty(self):
        return self.length == 0

pri_linked = Linked_Priority()
pri_linked.insert(11)
pri_linked.insert(12)