import heapq
# 일단 스코빌 최소가 k 이상일 때까지만 반복하면됨
# heap에 넣고 pop을 해. 이걸 값에 저장하고
# 또 팝을한거를 2배 곱해서 저장값에 더해서 다시 push  
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(scoville[0] < K):
        if len(scoville) == 1:
            return -1
        
        cnt = heapq.heappop(scoville)
        cnt += 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, cnt)
        answer += 1
    return answer