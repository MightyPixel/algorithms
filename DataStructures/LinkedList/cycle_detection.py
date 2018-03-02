"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head:
        return 0

    visited = [head.data]

    while head.next:
        if head.next.data in visited:
            return 1

        head = head.next

    return 0
