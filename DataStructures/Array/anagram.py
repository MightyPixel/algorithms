def deletions_needed(a, b):
    """
    Find the number of different elements
    """
    xs, ys = list(a), list(b)
    common = []

    for x in xs:
        if x in ys:
            ys.remove(x)
            common += [x]

    adiff = len(a) - len(common)
    bdiff = len(b) - len(common)

    return adiff + bdiff


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    print(deletions_needed(a, b))
