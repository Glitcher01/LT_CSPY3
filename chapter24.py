class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end="")
        if self.head is not None:
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

def print_list(node):
    list = []
    while node is not None:
        list.append(node.cargo)
        node = node.next
    print(list)


def remove_second(node):
    if node is None: return
    first = node
    second = node.next
    first.next = second.next
    second.next = None
    return second


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

