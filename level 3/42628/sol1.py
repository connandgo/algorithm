import heapq as hq
def solution(operations):
    que = []
    answer = []
    hq.heapify(que)
    for op in operations:
        m,n = op.split()
        if m == 'I':
            hq.heappush(que,int(n))
            # print(que)
        elif que and m == 'D':
            if n == '1':
                que.remove(max(que))
                # print(que)
            elif n == '-1':
                hq.heappop(que)    
                # print(que)
    if que:
        answer.append(max(que))
        answer.append(que[0])
        return answer
    return [0,0]