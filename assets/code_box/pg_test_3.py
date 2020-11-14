total_min = 2000000001

def bt(battery, mx, cnt,total):
    global total_min
    if(mx <= cnt):
        if( total_min > total ):
            total_min = total
    else:
        for b in battery:
            dum = (mx - cnt) // b[0]
            if(dum == 0):
                dum = 1
            if(total_min > dum * b[1] + total):
                bt(battery,mx , cnt+b[0] * dum, dum * b[1] + total)

def solution(n, battery):
    global total_min
    battery = sorted(battery,key = lambda battery : battery[0]/battery[1], reverse= True)
    bt(battery,n,0,0)
    return total_min


a = solution(50,[[10,100000],[4,35000],[1,15000]])
print(a)