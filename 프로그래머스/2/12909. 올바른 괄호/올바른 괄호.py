def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append("(")
        if c == ")":
            try:
                stack.pop()
            except:
                return False
    return len(stack) == 0