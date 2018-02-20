class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def sum_tree(t):
    if not t.left and t.right:
        return t.value

    left_sum = right_sum = 0

    if t.left:
        left_sum = sum_tree(t.left)
    if t.right:
        right_sum = sum_tree(t.right)

    return t.value + left_sum + right_sum


def hasPathWithGivenSum(t, s):
    if not t:
        return s == 0

    if sum_tree(t) == s:
        return True

    if t.left and hasPathWithGivenSum(t.left, s):
        return True

    if t.right and hasPathWithGivenSum(t.right, s):
        return True

    return False

def traverseTree(t):
    front = [t]
    result = []

    while front:
        element = front.pop(0)
        if not element:
            continue

        result.append(element.value)

        if element.left:
            front.append(element.left)
        if element.right:
            front.append(element.right)

    return result


def largestValuesInTreeRows(t):
    front = [(t, 0)]
    result = []

    layers = {}
    current_level = 0
    while front:
        element, level = front.pop(0)
        current_level = level

        if not element:
            continue

        if level in layers:
            layers[level] += [element.value]
        else:
            layers[level] = [element.value]

        if element.left:
            front.append((element.left, current_level + 1))
        if element.right:
            front.append((element.right, current_level + 1))

    result = [0] * len(layers)
    print(layers)
    for level, values in layers.items():
        result[level] = max(values)

    return result


def largestValuesInTreeRows2(t):
    front = [(t, 0)]
    result = []

    layer = []
    current_level = -1
    while front:
        element, level = front.pop(0)

        if layer and current_level < level:
            print(layer)
            result += [max(layer)]
            layer = []

        current_level = level

        if not element:
            continue

        layer += [element.value]

        if element.left:
            front += [((element.left, current_level + 1))]
        if element.right:
            front += [((element.right, current_level + 1))]

    if layer:
        result += [max(layer)]

    return result

def climbingStaircase(n, k):
    stack = [[]]
    result = []

    while stack:
        current = stack.pop()

        print(current)
        climbed_steps = sum(current)
        if n == climbed_steps:
            result += [current]

        for i in range(k, 0, -1):
            if i + climbed_steps <= n:
                stack += [current + [i]]

    return result



n1 = Tree(5)
n2 = Tree(3)
n3 = Tree(1)
n4 = Tree(4)

n1.left = n3
n1.right = n2
n3.left = n4


print(sum_tree(n1))
print(sum_tree(n2))
print(sum_tree(n3))
