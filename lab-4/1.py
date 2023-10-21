def bracket_balance(text):
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in text:
        if char not in brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return not stack


print(bracket_balance('([{}])'))
print(bracket_balance(')('))
print(bracket_balance('(((]]]'))
