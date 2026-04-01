#1753 최단거리
import heapq 
import sys 
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue 
        
        for next_node, cost in graph[now]:
            new_dist = dist + cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, v_node, w = map(int, input().split())
    graph[u].append((v_node, w))

distance = [INF] * (v + 1)

dijkstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])