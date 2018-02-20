import math


def firstDuplicate(xs):
    for x in xs:
        positive_x = abs(x)
        positive_x_index = positive_x - 1

        xs[positive_x_index] *= -1
        if xs[positive_x_index] > 0:
            return positive_x

    return -1


def firstNotRepeatingCharacter(string):
    alphabet_len = ord('z') - ord('a') + 1
    unique_letter_index = [None] * alphabet_len

    for index, character in enumerate(string):
        alphabet_position = ord(character) - ord('a')
        if unique_letter_index[alphabet_position] is None:
            unique_letter_index[alphabet_position] = index
        else:
            unique_letter_index[alphabet_position] = math.inf

    min_index = math.inf
    result = '_'

    for alphabet_position, first_occurence in enumerate(unique_letter_index):
        if first_occurence is not None and min_index > first_occurence:
            min_index = first_occurence
            result = chr(alphabet_position + ord('a'))

    if result != math.inf:
        return result
    else:
        return '_'


# print(firstNotRepeatingCharacter('abacabad'))


# print(firstNotRepeatingCharacter('abacabaabacaba'))
# print(firstNotRepeatingCharacter('z'))
# print(firstNotRepeatingCharacter('bcccccccb'))

# print(firstNotRepeatingCharacter('abcdefghijklmnopqrstuvwxyziflskecznslkjfabe'))
