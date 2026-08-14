def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False   
    return len(stack) == 0