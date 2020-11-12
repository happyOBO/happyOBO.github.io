import queue

def solution(priorities, location):
    answer = 0
    q_p = queue.Queue()
    q_l = queue.Queue()
    for p in range(len(priorities)):
        if( p == location):
            q_l.put(True)
        else:
            q_l.put(False)
        q_p.put(priorities[p])

    
    while(q_p.qsize() != 0):
        top_elm = q_p.get()
        is_mine = q_l.get()
        if(top_elm < max(q_p.queue)):
            q_p.put(top_elm)
            q_l.put(is_mine)
        else:
            answer +=1
            if(is_mine):
                return answer

    
    return answer

a = solution([10,9,8,7,1,2,4,5,18,2,2,1],10)
print(a)