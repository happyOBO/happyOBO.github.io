def solution(land):
    answer = 0
    ans_list = []
    N = len(land)
    for i in range(N):
        r = []
        for j in range(4):
            if (i == 0):
                r.append(land[i][j])
            else:
                r.append(0)
        ans_list.append(r)
    for i in range(1,N):
        for j in range(4):
            mx = 0
            for k in range(4):
                if( j != k):
                    if( ans_list[i-1][k] + land[i][j]  > mx):
                        mx = ans_list[i-1][k] + land[i][j] 
            ans_list[i][j] = mx
        for x in range(N):
            print(ans_list[x])
        print()
    mx = 0
    for i in range(4):
        if(mx < ans_list[N-1][i]):
            mx = ans_list[N-1][i]

    return mx


print(solution([ [5,3,4,2], [1,7,2,5], [1,2,3,1], [3,3,2,3]]))