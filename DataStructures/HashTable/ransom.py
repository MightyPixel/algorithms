def ransom_note(magazine, ransom):
    """
    Finds out if it is possible to create ransom with subset of magazine
    """
    if len(magazine) < len(ransom):
        return False

    mwords = {}
    for word in magazine:
        if word in mwords:
            mwords[word] += 1
        else:
            mwords[word] = 1

    for word in ransom:
        if not (word in mwords) or mwords[word] == 0:
            return False
        else:
            mwords[word] -= 1

    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
