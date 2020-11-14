import queue

def solution(n, computers):
    answer = 0
    is_visit = []
    do_nothing = True
    q = queue.Queue()
    for i in range(n):
        is_visit.append(-1)
    
    if(do_nothing): 
        q.get()
    for j in range(n):
        if(row != j and computers[row][j] == 1 ):
            q.put(j)
            do_nothing = False
    return answer