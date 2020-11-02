def solution(encrypted_text, key, rotation):
    answer = ''
    if(rotation > 0):
        for i in range(rotation):
            encrypted_text += encrypted_text[0]
            encrypted_text = encrypted_text[1:]
    
    else:
        for i in range(-rotation):
            encrypted_text = encrypted_text[-1] + encrypted_text
            encrypted_text = encrypted_text[:-1]
    
    for i in range(len(encrypted_text)):
        enc_num = ord(encrypted_text[i]) - 96
        key_num = ord(key[i]) -96
        total_num = (enc_num - key_num ) % 26 + 96
        print(enc_num,"+",key_num,"=",total_num)
        if(total_num == 96):
            total_num += 26
        answer += chr(total_num)
    
    return answer


a = solution("abce","zzzz", - 2)

print(a)