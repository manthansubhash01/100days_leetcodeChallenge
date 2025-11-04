import heapq

n,m = map(int,input().split())
n += 1
A = []

for i in range(m):
    u,v = map(int,input().split())
    A.append([u,v])

indegree = [0] * n
adjlst = [[] for _ in range(n)]

for u,v in A:
    indegree[v] += 1
    adjlst[u].append(v)

queue = []
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

topo_order = []

while queue:
    a = heapq.heappop(queue)
    topo_order.append(a)

    for i in adjlst[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue,i)
topo_order.pop(0)

if len(topo_order) != n-1:
    print("IMPOSSIBLE")
else:
    for i in topo_order:
        print(i,end = " ")