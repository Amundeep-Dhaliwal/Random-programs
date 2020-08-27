# this script can be used to ensure a string of parentheses is matched

# '{([])[()]}' - Matched returns 1
# '{[}]}' - Not matched returns 0

def isValidPair(left, right):
    if left + right == '()':
        return True
    elif left + right == '{}':
        return True
    elif left + right == '[]':
        return True
    return False

def solution(S):
    stack = []

    for symbol in S:
        if symbol in ('[', '{', '('):
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            lastsymb = stack.pop()
            if not isValidPair(lastsymb, symbol):
                return 0
    if len(stack) != 0:
        return 0
    return 1
