class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_child(root):
    if not root.left and not root.right:
        return root.data

    if not root.left and root.right:
        return max_child(root.right)
    if root.left and not root.right:
        return max(root.data, max_child(root.left))
    if root.left and root.right:
        return max(root.data, max_child(root.left), max_child(root.right))

def min_child(root):
    if not root.left and not root.right:
        return root.data

    if not root.left and root.right:
        return min_child(root.right)
    if root.left and not root.right:
        return min_child(root.left)
    if root.left and root.right:
        return min(root.data, min_child(root.left), min_child(root.right))

import sys

def is_bst(root, mini, maxi):
    if not root:
        return True

    if root.data < mini or root.data > maxi:
        return False

    return (is_bst(root.left, mini, root.data - 1) and is_bst(root.right, root.data + 1, maxi))

def checkBST(root):
    return is_bst(root, -sys.maxsize, sys.maxsize)

a = Node(4)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
g = Node(5)
f = Node(7)
#h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = g
c.right = f
#g.left = h
print(checkBST(a))
