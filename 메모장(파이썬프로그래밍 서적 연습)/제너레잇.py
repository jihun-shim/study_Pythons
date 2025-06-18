# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)

# graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
# bfs(graph, 1)  # 출력: 1 2 3 4

