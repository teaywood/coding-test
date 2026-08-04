def solution(ingredient):
    count = 0
    stack = []
    for food in ingredient:
        stack.append(food)
        if len(stack) > 3 and stack[-4:] == [1,2,3,1]:
            del stack[-4:]
            count += 1
    return count