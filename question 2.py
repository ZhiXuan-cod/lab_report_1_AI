# StudentID_Lab1.py
# BFS & DFS on the directed graph from Lab Report 1
# Alphabetical tie-breaking is applied when expanding nodes

from collections import deque

# -------------------------------------------------
# Graph (directed) – adjacency list
# -------------------------------------------------
graph = {
    'A': ['B'],
    'B': ['C', 'E', 'G'],
    'C': ['D'],
    'D': [],
    'E': ['H'],
    'G': ['F'],
    'H': [],
    'F': []
}

# -------------------------------------------------
# Helper: print a nicely formatted path
# -------------------------------------------------
def print_path(title, lines):
    print(f"\n{title}")
    print("\n".join(lines))

# -------------------------------------------------
# BFS – returns order, levels and step-by-step trace
# -------------------------------------------------
def bfs(start):
    visited = set()
    queue = deque([start])
    order = []
    levels = {start: 0}
    trace = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        trace.append(f"Visit {node} (level {levels[node]})")

        # neighbours alphabetically, only unvisited
        neighbours = sorted([n for n in graph[node] if n not in visited])
        for n in neighbours:
            if n not in levels:
                levels[n] = levels[node] + 1
            queue.append(n)
            trace.append(f"  → enqueue {n} (level {levels[n]})")

    return order, levels, trace

# -------------------------------------------------
# DFS – iterative version (stack) with trace
# -------------------------------------------------
def dfs(start):
    visited = set()
    stack = [start]
    order = []
    trace = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        trace.append(f"Visit {node}")

        # push neighbours in *reverse* alphabetical order
        # → the first letter in the alphabet will be popped first
        neighbours = sorted(graph.get(node, []), reverse=True)
        for n in neighbours:
            if n not in visited:
                stack.append(n)
                trace.append(f"  → push {n} onto stack")

    return order, trace

# -------------------------------------------------
# MAIN – run from node A (as in the question)
# -------------------------------------------------
if __name__ == "__main__":
    start_node = 'A'

    # ---------- BFS ----------
    bfs_order, bfs_levels, bfs_trace = bfs(start_node)
    print_path("BREADTH-FIRST SEARCH (BFS)", [
        f"Traversal order : {' → '.join(bfs_order)}",
        "Levels          : " + ", ".join(f"{node}: {lvl}" for node, lvl in bfs_levels.items())
    ])
    print_path("BFS step-by-step", bfs_trace)

    # ---------- DFS ----------
    dfs_order, dfs_trace = dfs(start_node)
    print_path("DEPTH-FIRST SEARCH (DFS)", [
        f"Traversal order : {' → '.join(dfs_order)}"
    ])
    print_path("DFS step-by-step", dfs_trace)

    # ---------- Complexity ----------
    print("\nTIME & SPACE COMPLEXITY")
    print("BFS : O(V + E) time, O(V) space")
    print("DFS : O(V + E) time, O(V) space")