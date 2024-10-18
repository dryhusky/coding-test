# 소요시간 : 10m
# 구현할 때 lmabda가 생각나서 사용해봄

def solution(sides):
    answer = 0

    largest = max(sides)
    sides.remove(largest)
    other = sum(sides) 

    check = lambda large,other : 1 if other>large else 2
    answer = check(largest,other)

    return answer
