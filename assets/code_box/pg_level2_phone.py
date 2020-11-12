def solution(phone_book):
    # answer = True
    phone_book.sort(key = len)
    N = len(phone_book)
    for i in range(N):
        for j in range(i+1,N):
            if(phone_book[i] == phone_book[j][0:len(phone_book[i])]):
                return False
    return True