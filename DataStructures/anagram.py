def number_needed(a, b):
    # Find #common_letters
    # substract from len(a) - len(common_letters)
    # substract from len(B) - len(common_letters)
    # add and return
    common = []
    # a = 'abbc'
    # b = 'bbb'

    x, y = list(a), list(b)

    for l in x:
        if l in y:
            y.remove(l)
            common += [l]


    adiff = len(a) - len(common)
    bdiff = len(b) - len(common)
    # print(common, adiff, bdiff, len(a), len(b), len(common))
    return adiff + bdiff


a = input().strip()
b = input().strip()

print(number_needed(a, b))
