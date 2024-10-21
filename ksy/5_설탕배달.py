weight = int(input())
zero_list = []

min_loof = weight // 3 + 1

for x in range(min_loof):
    for y in range(min_loof):
        if x == 0 and y == 0 :
            continue
        elif weight - 5*x - 3*y == 0:
            zero_list.append(x+y)

if zero_list:
    print(min(zero_list))
else:
    print('-1')