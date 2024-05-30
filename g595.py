# g595. 1. 修補圍籬
n = int(input())
ary = list(map(int,input().split()))
total = 0
for idx,val in enumerate(ary):
    if val == 0:
        if idx == 0 :
            num = ary[idx+1]
        elif idx == len(ary) - 1:
            num = ary[idx-1]
        else:
            num = min(ary[idx-1],ary[idx+1])
        total += num
print(total)