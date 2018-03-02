class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def print_linked_list(l):
    result = []
    while l:
        result.append(str(l.value))
        l = l.next
    print('->'.join(result))

def get_linked_list(l):
    start = linked_list = ListNode(l[0])
    for e in l[1:]:
        linked_list.next = ListNode(e)
        linked_list = linked_list.next

    return start


def removeKFromList(l, k):
    result = []

    while l:
        if l.value != k:
            result.append(l.value)
        l = l.next

    return result

def reverse_linked_list(l):
    current = l
    back = None
    forward = current.next

    while forward:
        current.next = back
        back = current
        current = forward
        forward = forward.next

    current.next = back

    return current


def isListPalindrome(l):
    if not l:
        return True

    r = l
    start = l
    n = 0

    while r:
        r = r.next
        n += 1

    for i in range(n//2):
        l = l.next

    l = reverse_linked_list(l)

    for i in range(n//2):
        if start.value != l.value:
            return False
        start = start.next
        l = l.next

    return True

# a = get_linked_list([1, 2, 3, 2, 1])
# print(isListPalindrome(a))

def sum_nodes(a, b):
    c = a + b
    overflow = int(c / 10000)
    result = c % 10000

    return result, overflow

def addTwoHugeNumbers(a, b):
    if not a:
        return b
    if not b:
        return a

    rev_a = reverse_linked_list(a)
    rev_b = reverse_linked_list(b)

    s, overflow = sum_nodes(rev_a.value, rev_b.value)
    head = total = ListNode(s)

    rev_a = rev_a.next
    rev_b = rev_b.next

    if overflow:
        if not rev_a:
            rev_a = ListNode(overflow)
            overflow = 0
        elif not rev_b:
            rev_b = ListNode(overflow)
            overflow = 0

    while rev_a and rev_b:
        s, next_overflow = sum_nodes(rev_a.value, rev_b.value)
        total.next = ListNode(s + overflow)
        total = total.next

        overflow = next_overflow

        rev_a = rev_a.next
        rev_b = rev_b.next


        if next_overflow:
            if not rev_a:
                rev_a = ListNode(next_overflow)
                overflow = 0
            elif not rev_b:
                rev_b = ListNode(next_overflow)
                overflow = 0

    if rev_a:
        total.next = rev_a
    if rev_b:
        total.next = rev_b


    return reverse_linked_list(head)


a = get_linked_list([9876, 5432, 1999])
b = get_linked_list([1, 8001])

print_linked_list(a)
print('+')
print_linked_list(b)
print('=')
print_linked_list(addTwoHugeNumbers(a, b))

print('----\n')

a = get_linked_list([123, 4, 5])
b = get_linked_list([100, 100, 100])

print_linked_list(a)
print_linked_list(b)

print_linked_list(addTwoHugeNumbers(a, b))


def add_lists(a, b):
    a = get_linked_list(a)
    b = get_linked_list(b)
    print('----\n')
    print_linked_list(addTwoHugeNumbers(a, b))

add_lists([1], [9998, 9999, 9999, 9999, 9999, 9999])
add_lists([1, 0, 1, 0, 1], [1, 0, 1])
add_lists([9999], [9999])
add_lists([9999], [0])
add_lists([9999], [1])
add_lists([0], [1])
add_lists([9999, 0], [1])
add_lists([9999, 0], [1, 1])
add_lists([9999, 0, 9999], [1, 0, 1])
add_lists([9999, 0, 1], [1, 0, 9999])
add_lists([9999, 9999, 9999], [0, 0, 0])
add_lists([9999, 9999, 9999], [0, 1, 0])
add_lists([1], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999])


a = get_linked_list([1, 2, 3])
b = get_linked_list([4, 5, 6])

def mergeTwoLinkedLists(l1, l2):
    current = start = None

    while l1 and l2:
        if l1.value < l2.value:
            if current:
                prev = current
                current = ListNode(l1.value)
                prev.next = current
            else:
                current = ListNode(l1.value)

            l1 = l1.next
        else:
            if current:
                prev = current
                current = ListNode(l2.value)
                prev.next = current
            else:
                current = ListNode(l2.value)

            l2 = l2.next

        if not start:
            start = current
    else:
        if not current and not start:
            if l1:
                start = l1
            else:
                start = l2
        elif l1:
            current.next = l1
        elif l2:
            current.next = l2

    return start

def rev_list(start, prev, k):
    p = start
    c = p.next
    n = c.next

    for i in range(k - 1):
        if not n:
            break

        c.next = p
        p = c
        c = n
        n = c.next

    if n:
        start.next = n

    if prev:
        prev.next = c
        return prev
    else:
        return start


# a = get_linked_list([1, 2, 3])
# r = rev_list(a, None, 3)

# print_linked_list(a)
# print_linked_list(r)


def reverseNodesInKGroups(l, k):
    start = l

    while l:
        print_linked_list(l)
#         l = rev_list(l, k)

    return start


# print_linked_list(mergeTwoLinkedLists(a, b))
# print_linked_list(mergeTwoLinkedLists(get_linked_list([1, 1]), get_linked_list([0])))
# print_linked_list(reverseNodesInKGroups(get_linked_list([1, 2, 3, 4, 5]), 2))
