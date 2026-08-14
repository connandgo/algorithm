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
                answer = False
    if stack:
        answer = False    
    return answer