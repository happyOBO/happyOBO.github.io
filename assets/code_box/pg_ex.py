def solution(v):
    answer = []
    rectan = [[],[]]
    for tup in v:
        for j in range(2):
            cnt = rectan[j].count(tup[j])
            if(cnt == 0):
                rectan[j].append(tup[j])
            elif(cnt == 1):
                rectan[j].remove(tup[j])
    answer = [rectan[0][0] , rectan[1][0]]
    

    return answer

a = solution([[1, 4], [3, 4], [3, 10]])

print(a)