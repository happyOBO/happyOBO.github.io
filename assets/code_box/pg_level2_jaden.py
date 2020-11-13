def solution(s):
    answer = ''
    list_s = list(s)
    for i in range(len(list_s)):
        if(i == 0 or list_s[i-1] == ' '):
            if(97 <= ord(list_s[i]) <= 122):
                list_s[i] = chr(ord(list_s[i]) -32)
        elif(list_s[i-1] != ' ' and 65 <= ord(list_s[i]) <= 90):
            list_s[i] = chr(ord(list_s[i]) +32)
    
    answer = ''.join(list_s)

    return answer

a = solution("3people unFollowed me")

print(a)