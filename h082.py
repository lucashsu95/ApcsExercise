from typing import Any


class Player:
    def __init__(self,s,t,idx) -> None:
        self.s = s
        self.t = t
        self.idx = idx
        self.loseCount = 0
    
    def __str__(self) -> str:
        return f"s: {self.s}, t: {self.t}, idx: {self.idx}, loseCount: {self.loseCount}"

    def isDie(self):
        if self.loseCount == m:
            return True
        return False
    
n,m = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(3)]
peopleNum = len(people[0])

battle = [Player(people[0][i],people[1][i],people[2][i]) for i in range(peopleNum)]
# battle.sort(key=lambda x:x.idx)
while len(battle) != 1:
    for i in range(1,len(battle),2):
        p1 = battle[i - 1]
        p2 = battle[i]
        # print(p1,p2)
        if p1.s * p1.t >= p2.s * p2.t:
            s = p1.s
            p1.s = int(p1.s + p2.s * p2.t / (2 * p1.t))
            p1.t = int(p1.t + p2.s * p2.t / (2 * s))
            p2.s += p2.s // 2
            p2.t += p2.t // 2
            p2.loseCount += 1
        else:
            s = p2.s
            p2.s = int(p2.s + p1.s * p1.t / (2 * p2.t))
            p2.t = int(p2.t + p1.s * p1.t / (2 * s))
            p1.s += p1.s // 2
            p1.t += p1.t // 2
            p1.loseCount += 1
        

    battle2 = []
    for p in battle:
        if not p.isDie():
            battle2.append(p)
        battle = battle2.copy()

for i in battle:
    print(i)
