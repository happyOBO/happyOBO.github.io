def multi(lst):
    mt = 1
    for i in lst:
        mt =  mt * (ord(i) - 48)
    return mt  

def solution(num):
    answer = 0
    while(True):
        num_list = str(num)
        num_list = list(num_list)
        N = len(num_list)
        if(N % 2 == 0):
            if(multi(num_list[: N//2]) == multi(num_list[N//2 :]) ):
                return num
            else:
                num += 1
        else:
            num = 10 ** N



a = solution(3462)
print(a)