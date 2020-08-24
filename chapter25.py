import re

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)

def eval_postfix(expr):
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    print(token_list)
    for token in token_list:
        if token is '' or token is ' ':
            continue
        if token is '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token is '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()


something = Stack()