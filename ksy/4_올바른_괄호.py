def solution(s):
# 2h25m
    answer = True

    stack = []

    for st in s:
        try : 
            if st == ")":
                stack.pop() 
            else:
                stack.append(st) # stack 에는 ")"만 
        except Exception as e: # 짝이 맞지 않다면 False
            answer = False
    return answer and len(stack) ==0