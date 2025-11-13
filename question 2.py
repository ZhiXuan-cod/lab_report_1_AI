from collections import deque

class Graph:
    def __init__(self):
        self.adj = {
            'A': ['D', 'E'],
            'B': ['A', 'C', 'G'],
            'C': [],
            'D': [],
            'E': ['H'],
            'G': ['F'],
            'F': [],
            'H': []
        }

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        order = []
        level = {start: 0}
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for nei in sorted(self.adj[node]):  # Alphabetical
                if nei not in visited and nei not in queue:
                    queue.append(nei)
                    level[nei] = level[node] + 1
        return order, level

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for nei in sorted(self.adj[node], reverse=True):  # Reverse for stack
                if nei not in visited:
                    stack.append(nei)
        return order