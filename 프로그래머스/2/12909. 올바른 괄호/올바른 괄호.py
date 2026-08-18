def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        if ["(",")"] == stack[-3:-1]:
             del stack[-3:-1]
    if ["(",")"] == stack:
             stack = []
    return not stack or False