import sys

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def find_path_to_child(self, name):
        path_to_child = [self.name]
        frontier = [[self]]

        while frontier:
            current_path = frontier.pop(0)
            current = current_path[-1]

            if not current:
                continue

            if current.name == name:
                return current_path

            frontier += [current_path + [current.left], current_path + [current.right]]

        return None

    def add_child(self, child):
        if self.left:
            self.right = TreeNode(child)
        else:
            self.left = TreeNode(child)

    def __str__(self):
        return self.name + '(' + str(self.left) + ', ' + str(self.right) + ')'


def OutputCommonManager(total_employees):
    employee_a = input()
    employee_b = input()

    root = None

    for line in sys.stdin:
        manager, employee = map(lambda s: s.strip(), line.split(' '))
        if not root:
            root = TreeNode(manager)

        parent = root.find_path_to_child(manager)[-1]
        parent.add_child(employee.strip())

    path_a = root.find_path_to_child(employee_a)
    path_b = root.find_path_to_child(employee_b)

    common_parent_name = path_a[0].name

    while path_a[1:] and path_b[1:]:
        if path_a[1] == path_b[1]:
            common_parent_name = path_a[1].name

        path_a = path_a[1:]
        path_b = path_b[1:]

    print(common_parent_name)

_count = int(input())
OutputCommonManager(_count)

