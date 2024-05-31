# f313. 2. 人口遷移

r,c,k,m = map(int,input().split())

ls = [list(map(int,input().split())) for _ in range(r)]
for _ in range(m):
    ary = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if ls[y][x] == -1 :continue
            
            num = int(ls[y][x] / k)
            if y != 0 and ls[y-1][x] != -1:
                ary[y-1][x] += num
                ary[y][x] -= num

            if y != r - 1 and ls[y+1][x] != -1:
                ary[y+1][x] += num
                ary[y][x] -= num
            
            if x != 0 and ls[y][x-1] != -1:
                ary[y][x-1] += num
                ary[y][x] -= num

            if x != c - 1 and ls[y][x+1] != -1:
                ary[y][x+1] += num
                ary[y][x] -= num
                
    for y in range(r):
        for x in range(c):
            ls[y][x] += ary[y][x]

minNum = maxNum = ls[0][0]
for i in ls:
    for j in i:
        if j == -1 :continue
        minNum = min(minNum,j)
        maxNum = max(maxNum,j)
        
print(minNum)
print(maxNum)