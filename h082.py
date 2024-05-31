def main():
    n, m = map(int, input().split())

    s = [0] * (n + 1)
    t = [0] * (n + 1)
    lose = [0] * (n + 1)

    for i in range(1, n + 1):
        s[i] = int(input())  # 战力

    for i in range(1, n + 1):
        t[i] = int(input())  # 应变力

    v = [int(input()) for _ in range(n)]  # 第一轮进行配对竞赛的玩家编号

    while len(v) > 1:
        v1, v2 = [], []
        for i in range(0, len(v) - 1, 2):
            x, y = v[i], v[i + 1]
            a, b, c, d = s[x], t[x], s[y], t[y]
            if a * b >= c * d:
                s[x] += c * d // (2 * b)
                t[x] += c * d // (2 * a)
                s[y] += c // 2
                t[y] += d // 2
                v1.append(x)
                lose[y] += 1
                if lose[y] < m:
                    v2.append(y)
            else:
                s[y] += a * b // (2 * d)
                t[y] += a * b // (2 * c)
                s[x] += a // 2
                t[x] += b // 2
                v1.append(y)
                lose[x] += 1
                if lose[x] < m:
                    v2.append(x)

        if len(v) % 2 == 1:
            v1.append(v[-1])
        
        v = v1 + v2

    print(v[0])

if __name__ == "__main__":
    main()
