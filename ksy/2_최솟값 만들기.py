def solution(A,B):
    answer = 0
    
    a_sort = sorted(A)
    b_reverse_sort = sorted(B, reverse = True)
    
    for a,b in zip(a_sort,b_reverse_sort):
        answer+=a*b

    return answer