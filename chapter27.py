import pickle

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def total(tree):
    if tree is None: return 0
    return total(tree.left) + tree.cargo + total(tree.right)


def print_tree_prefix(tree):
    if tree is None: return
    print(tree.cargo, end=' ')
    print_tree_prefix(tree.left)
    print_tree_prefix(tree.right)


def print_tree_postfix(tree):
    if tree is None: return
    print_tree_postfix(tree.left)
    print_tree_postfix(tree.right)
    print(tree.cargo, end=' ')


def print_tree_inorder(tree, level=0):
    if tree is None: return
    if str(tree.cargo) in '*+-/' and level > 0: print('(', end='')
    print_tree_inorder(tree.left, level + 1)
    print(tree.cargo, end='')
    print_tree_inorder(tree.right, level + 1)
    if str(tree.cargo) in '*+-/' and level > 0: print(')', end='')


def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level + 1)
    print(" " * level + str(tree.cargo))
    print_tree_indented(tree.left, level + 1)


def create_token_list(exp_str):
    token_list = []
    for i in exp_str:
        try:
            token_list.append(int(i))
        except:
            if i != ' ' and i != '':
                token_list.append(str(i))
    token_list.append('end')
    return token_list


def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False


def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list, ')'):
            raise ValueError('missing closed parenthesis')
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x)


def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree('*', a, b)
    return a


def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree('+', a, b)
    return a


def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"


def animal(begin=Tree("bird")):
    # Start with a singleton
    root = begin

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "):
            pickle.dump(root, open('saved_tree.pickle', 'wb'))
            break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt = "What is the animal's name? "
        animal = input(prompt)
        prompt = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

        prompt = 'Do you want to go again?'
        if yes(prompt):
            continue
        else:
            pickle.dump(root, open('saved_tree.pickle', 'wb'))
            break

animal()
f = open('saved_tree.pickle', 'rb')
example = pickle.load(f)
print_tree_indented(example)
