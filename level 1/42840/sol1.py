def solution(answers):
    answer = []
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]
    ms1 = ms2 = ms3 = 0
    
    for i in range(len(answers)):
        if answers[i] == m1[i % 5]:
            ms1 += 1
        if answers[i] == m2[i % 8]:
            ms2 += 1
        if answers[i] == m3[i % 10]:
            ms3 += 1
    score_dict = {1 : ms1, 2 : ms2, 3 : ms3}
    ms = max(ms1, ms2, ms3)
    for key, value in score_dict.items():
        if value == ms:
            answer.append(key)
    return answer