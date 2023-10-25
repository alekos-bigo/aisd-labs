def bracket_balance(text):
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = []
    for i, char in enumerate(text):
        if char not in brackets:
            stack.append(char)
        else:
            if not stack:
                return i
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return i
    return not stack


print(bracket_balance('([{}])'))
print(bracket_balance(')('))
print(bracket_balance('(((]]]'))
