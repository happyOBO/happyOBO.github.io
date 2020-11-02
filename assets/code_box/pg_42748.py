def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        parts = array[i-1:j]
        parts.sort()
        answer.append(parts[k-1])
    return answer


# an = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
# print(an)