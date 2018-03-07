class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data) + '(' + str(self.left) + ', ' + str(self.right) + ')'



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

def lca(root, v1, v2):
    """
    Return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.
    """
    if v1 < root.data < v2 or v2 < root.data < v1 or root.data == v1 or root.data == v2:
        return root
    if v1 < root.data and v2 < root.data:
        return lca(root.left, v1, v2)
    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)

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
print(a)
print(checkBST(a))
print(lca(a, 3, 5).data)
print(lca(a, 1, 3).data)
print(lca(a, 4, 7).data)
print(lca(a, 7, 4).data)

