import re
def solution(new_id):
    answer = ''
    # step 1
    new_id = new_id.lower()
    # step 2
    answer = re.sub(r'[^\da-z-_.]','',new_id)
    # step 3
    answer = re.sub(r'\.+', '.', answer)
    # step 4
    answer = answer.strip('.')
    # step 5
    if not answer:
        answer += 'a'
    # step 6
    if len(answer) > 15:
        answer = answer[:15].strip('.')
    # step 7
    answer = answer.ljust(3, answer[-1])
    return answer
