def check(arr):
    st = []
    for ar in arr:
        if( ar == '('):
            st.append('(')
        else:
            if( len(st) != 0 and st[-1] == '('):
                st.pop()
            else:
                return False
    if(len(st) != 0):
        return False
    else:
        return True

def solution(arr1, arr2):
    answer = 0
    for a_1 in arr1:
        for a_2 in arr2:
            merge = a_1+ a_2
            if(merge[0] == ')'):
                pass
            else:
                st = []
                is_false = True
                for ar in merge:
                    if( ar == '('):
                        st.append('(')
                    else:
                        if( len(st) != 0 and st[-1] == '('):
                            st.pop()
                        else:
                            is_false = False
                if(len(st) != 0):
                    is_false = False
                if(is_false):
                    answer += 1
                    
    return answer



a = solution(["()", "(()", ")()", "()"],[")()", "()", "(()"])

print(a)