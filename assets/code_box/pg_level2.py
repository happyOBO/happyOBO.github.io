total = 0
def search_dic(dic, kd):
    if(len(dic) == 0):
        return -1
    else:
        for i in range(len(dic)):
            if(dic[i][0] ==  kd):
                return i
    return -1

def backtr(arr,mx,cur,sm):
    global total
    # print(arr)
    if(mx == cur ):
        total += sm
    elif(len(arr) == 0):
        pass
    else:
        for i in range(len(arr)):
            # print(arr)
            backtr(arr[i+1:],mx,cur+1,sm * arr[i])

def solution(clothes):
    cloth_dic = []
    for tup in clothes:
        idx = search_dic(cloth_dic, tup[1])
        if(-1 != idx ):
            cloth_dic[idx].append(tup[0])
        else :
            cloth_dic.append([tup[1], tup[0]])
    cloth_counts = []
    for cl in cloth_dic:
        cloth_counts.append(len(cl) -1)

    # print(cloth_counts)

    for i in range(len(cloth_counts)):
        backtr(cloth_counts,i+1,0,1)
    answer = total

    return answer

a = solution([["yellow_hat", "headgear"],["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

print(a)