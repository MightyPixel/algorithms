def is_matched(expression):
    """
    Finds if expression is valid in terms of opened/closed brackets
    """
    brackets = []
    oppening_bracket = ['(', '{', '[']
    matching_bracket = {'(': ')', '{': '}', '[': ']'}
    # {[()]}
    for bracket in expression:
        if bracket in oppening_bracket:
            brackets.append(bracket)
        else:
            try:
                last_bracket = brackets.pop()
                if matching_bracket[last_bracket] != bracket:
                    return False
            except IndexError:
                return False

    return len(brackets) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
