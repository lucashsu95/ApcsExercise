# f163. 貨物分配 wa
# https://zerojudge.tw/ShowProblem?problemid=f163
class Tree:
    def __init__(self, name, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.name = name

    def __str__(self):
        return f'{self.name} {self.value}'
    
    def getWeight(self):
        total_weight = self.value if self.value is not None else 0
        if self.left is not None:
            total_weight += self.left.getWeight()
        if self.right is not None:
            total_weight += self.right.getWeight()
        return total_weight
    
    def insertNode(self,node):
        if self.left is None:
            self.left = Tree(node,node)
            return self.name

        if self.right is None:
            self.right = Tree(node,node)
            return self.name

        if self.left.getWeight() > self.right.getWeight():
            return self.right.insertNode(node)
        else:
            return self.left.insertNode(node)

n,m = map(int,input().split())
weight = list(map(int,input().split()))
data = list(map(int,input().split()))

nodes = {}
for _ in range(n - 1):
    a,b,c = map(int,input().split())
    if a not in nodes:
        nodes[a] = Tree(a)
    if b not in nodes:
        nodes[b] = Tree(b)
    if c not in nodes:
        nodes[c] = Tree(c)

    nodes[a].left = nodes[b]
    nodes[a].right = nodes[c]

root = nodes[1]

# 加重量去
for w in range(n ,2 * n):
    nodes[w].value = weight[w - n]
    
for d in data:
    print(root.insertNode(d),end=' ')