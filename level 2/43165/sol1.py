def solution(numbers, target):
    def dfs(idx, total):
        if idx == len(numbers):
            return 1 if total == target else 0
        add = dfs(idx + 1, total + numbers[idx])
        sub = dfs(idx + 1, total - numbers[idx])
        return add + sub
    return dfs(0, 0)