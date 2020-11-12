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
    mx = 0
    for i in range(4):
        if(mx < ans_list[N-1][i]):
            mx = ans_list[N-1][i]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return mx