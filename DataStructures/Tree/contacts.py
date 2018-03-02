class Node:
    def __init__(self):
        self.children = {}
        self.is_complete_word = False
        self.children_count = 0

    def __str__(self):
        result = str(self.children) + ' ' + str(self.is_complete_word)

        for child in self.children:
            result += str(self.children[child])

        return result

def add_contact(contacts, name):
    current = contacts

    for c in name:
        if c in current.children:
            current = current.children[c]
        else:
            current.children[c] = Node()
            current = current.children[c]

        current.children_count += 1

    current.is_complete_word = True

    return current

def count_children(parent):
    result = int(parent.is_complete_word)
    if not parent.children:
        return result

    for child in parent.children:
        result += count_children(parent.children[child])

    return result


def find_contact(contacts, name):
    current = contacts

    for c in name:
        if c in current.children:
            current = current.children[c]
        else:
            return 0

    return current.children_count



contacts = Node()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add_contact(contacts, contact)
    elif op == 'find':
        print(find_contact(contacts, contact))

