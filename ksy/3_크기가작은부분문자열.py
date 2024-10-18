# 6m

def solution(t, p):
    answer = 0
    p_len = len(p)
    
    
    for idx in range(len(t)-p_len+1):
        if t[idx:(idx+p_len)] <= p:
            answer+=1
    
    return answer