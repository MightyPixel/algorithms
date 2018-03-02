def array_left_rotation(xs, d):
    """
    rotates xs left with d positions
    pythonic way
    """
    return xs[d:] + xs[:d]

def array_left_rotation_juggling(xs, d):
    """rotates xs left with d positions constant memory"""
    # return a[d:] + a[:d]
    # TODO
    n = len(xs)

    current_index = start = n - 1
    prev_backup = xs[current_index]
    s = 1

    for i in range(n - 1):
        next_index = current_index - d
        if next_index < 0:
            next_index += n
        if next_index == start:
            current_index -= s
            start = current_index
            s += 1

        print(xs, current_index, next_index)

        backup = xs[next_index]
        xs[next_index] = prev_backup
        prev_backup = backup
        current_index = next_index


    return xs

print([1, 2, 3, 4, 5, 6])
print(array_left_rotation([1, 2, 3, 4, 5, 6], 3))


if __name__ == '__main__':
    _, d = map(int, input().strip().split(' '))
    xs = list(map(int, input().strip().split(' ')))
    rotated_xs = array_left_rotation(xs, d);
    print(' '.join(map(str, rotated_xs)))
