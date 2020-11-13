
def solution(board, moves):
    answer = 0
    depth = []
    stack = []
    pre_doll = -1
    N = len(board)
    M = len(board[0])
    for i in range(M):
        depth.append(-1)
    for i in range(N):
        for j in range(M):
            if( board[i][j] == 0):
                depth[j] = i

    for m in moves:
        if(depth[m-1] < M-1):
            print(depth)
            pick = board[depth[m-1]+1][m-1]
            if(len(stack) == 0 or stack[-1] != pick):
                stack.append(pick)
            elif(stack[-1] == pick):
                # print(stack," pick[",depth[m-1]+1,"][",m-1,"] :",pick)
                stack.pop()
                answer += 2
            depth[m-1] += 1
        
    return answer

a = solution([[11,21,31,41,51],[51,41,31,21,11],[11,21,31,41,51],[51,41,11,21,11],[11,21,31,41,51]],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])

print(a)