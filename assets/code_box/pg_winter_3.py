import queue

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# 시작점에 대한 모든 노드의 최단거리 값 계산
def solution(arr):
    N = len(arr)
    M = len(arr)
    answer = [ 0,0,0]
    check = []
    for s in range(len(arr)):
        row_check = []
        for k in range(len(arr)):
            row_check.append(-1)
        check.append(row_check)

    for idx_i in range(len(arr)):
        for idx_j in range(len(arr)):
            strt_x = idx_i
            strt_y = idx_j
            dst_x = N
            dst_y = M
            real = False
            q = queue.Queue()
            # 맵 최단거리 값 누적 표시하는 check 생성

            # 시작 초기화
            # print(i,j)
            if(check[strt_x][strt_y] != -1):
                continue
            else:
                real = True
            check[strt_x][strt_y] = 1
            q.put((strt_x,strt_y))
            # bfs 시작
            while (q.qsize() != 0):
                x = q.queue[0][0]
                y = q.queue[0][1]
                last = q.get()
                # print(last)
                for i in range(4):
                    xx = x + dir[i][0]
                    yy = y + dir[i][1]
                    if (xx < 0 or xx >= N or yy < 0 or yy >= M):
                        continue
                    # 못가는 곳이거나 이미 지나쳤던 곳이면 push 하지 않는다.
                    if (arr[xx][yy] != arr[idx_i][idx_j] or check[xx][yy] != -1):
                        continue
                    # 옆 노드에서 조건에 맞는 상하 좌우 노드는 거리가 1 증가하면 갈수 있다.
                    check[xx][yy] = check[x][y] + 1
                    # push
                    q.put((xx, yy))
            if(real):
                answer[arr[idx_i][idx_j]] +=1
                real = False
    return answer



# check = solution([[0,0,1],[2,2,1],[0,0,0]])
# print("최단거리 맵")
# for i in range(3):
#     for j in range(3):
#         print('{0:^2d}'.format(check[i][j]),end = ",")
#     print()


# # [[0,0,1,1]
# #  [1,1,1,1]
# #  [2,2,2,1]
# #  [0,0,0,2]]


# # [[0,0,1]
# #  [2,2,1]
# #  [0,0,0]]