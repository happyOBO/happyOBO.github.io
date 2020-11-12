def solution(s):
    answer = [0,0]
    while(s != '1'):
        answer[1] += s.count("0")
        answer[0] += 1
        l_s = []
        for i in s:
            if(i == "1"):
                l_s.append("1")
        s = bin(len(l_s))
        s = s[2:]
    return answer


a = solution("110010101001")

print(a)
