def solution(new_id):
    answer = ''
    # step 1
    new_id = new_id.lower()
    # step 2
    for id in new_id:
        if id.isdigit() or id.islower() or id in ('-','_','.'):
            answer += id
    # step 3
    while('..' in answer):
        answer = answer.replace('..','.')
    # step 4
    answer = answer.strip('.')
    # step 5
    if not answer:
        answer += 'a'
    # step 6
    if len(answer) > 15:
        answer = answer[:15].strip('.')
    # step 7
    while(len(answer) < 3):
        answer += answer[-1]
    return answer
