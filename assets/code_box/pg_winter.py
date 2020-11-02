def solution(n, delivery):
    answer = ''
    ans_list = []
    for i in range(n):
        ans_list.append('?')
    for de in delivery:
        if(de[2] == 1):
            ans_list[de[0] -1] = 'O'
            ans_list[de[1] -1] = 'O'

    for de in delivery:
        if(de[2] == 0):
            if(ans_list[de[0] -1 ] == 'O'):
                ans_list[de[1] - 1] = 'X'
            elif(ans_list[de[1] -1] == 'O'):
                ans_list[de[0] - 1] = 'X'
    

    for i in range(n):
        answer += ans_list[i]
    return answer


a = solution(7,[[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]])

print (a)