#1238 파티
import heapq 
import sys 

input = sys.stdin.readline
INF = float('inf')
def dijstra(start, target_graph):

    distance = [INF] * (n + 1)
    distance[start] = 0

    # heapq 
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        d, now = heapq.heappop(pq)

        if distance[now] < d:
            continue 

        for next_node, dist in target_graph[now]:
            cost = d + dist 

            if cost < distance[next_node]:
                distance[next_node] = cost 
                heapq.heappush(pq, (cost, next_node))
    
    return distance     

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    rev_graph[e].append((s, t))


dist_back = dijstra(x, graph)
dist_go = dijstra(x, rev_graph)

max_time = 0
for i in range(1, n + 1):
    max_time = max(max_time, dist_go[i] + dist_back[i])

print(max_time)