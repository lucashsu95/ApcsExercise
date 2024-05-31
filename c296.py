# APCS-2016-1029-3 定時K彈 (老實說我還是不太懂為什麼是n - k + 1答案就可以出來了)

def fun(n, m, k):
    res = 0
    for i in range(n - k + 1, n + 1):
        res = (res + m) % i
    return res + 1

n, m, k = map(int, input().split()) # 總人數、間隔數、以及 K 值
print(fun(n, m, k))