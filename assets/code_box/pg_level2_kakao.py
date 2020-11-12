def check(i,j,board):
    pre = board[i][j]
    for x in range(2):
        for y in range(2):
            if(pre != board[i+x][j+y] or board[i+x][j+y] == "X"):
                return False
    return True



def solution(m, n, board):
    is_excute = True
    board_list = []
    answer = 0
    for i in range(m):
        r_b = []
        for j in range(n):
            r_b.append(board[i][j])
        board_list.append(r_b)
    while(is_excute):
        is_excute = False
        res = []
        for i in range(m):
            r = []
            r_b = []
            for j in range(n):
                r.append(0)
                r_b.append(board[i][j])
            res.append(r)
            board_list.append(r_b)
            

        for i in range(m-1):
            for j in range(n-1):
                if(check(i,j, board_list)):
                    is_excute = True
                    for x in range(2):
                        for y in range(2):
                            res[i+x][j+y] = 1

        # for i in range(m):
        #     print(res[i])
        

        for i in range(m):
            for j in range(n):
                if( i+1 < m and res[i+1][j] == 1):
                    for k in range(0,i+1):
                        board_list[i+1-k][j] = board_list[i-k][j]
                        board_list[i-k][j] = "X"
    
        for i in range(m):
            print(board_list[i])

        print()

    for i in range(m):
        for j in range(n):
            if(board_list[i][j] == "X"):
                answer += 1
    return answer


a = solution(4,6,["CCBDEF", "AAADEF", "AAABFF", "CCBBFF" ])

print(a)


# "CCBDE"
# "AAADE"
# "AAABF"
# "CCBBF"