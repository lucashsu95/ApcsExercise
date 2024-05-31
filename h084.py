# h084. 4. 牆上海報

n,k = map(int,input().split())
h = list(map(int,input().split())) # board
w = list(map(int,input().split())) # seal


l, r = 1, max(h) + 1 # 高度,

while r - l > 1:
    mid = (l + r) // 2
    cnt = 0
    now = 0
    flag = False
    
    for height in h:
        if height >= mid:
            cnt += 1
            if cnt >= w[now]:
                cnt -= w[now]
                now += 1
                if now == k:
                    flag = True
                    break
        else:
            cnt = 0
    
    if flag:
        l = mid
    else:
        r = mid

print(l)