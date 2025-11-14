# --------------------------------------------------------------
#  Graph definition (based on the directed graph in the image:
#  A -> B, B -> C (with C -> B cycle), B -> D (with D -> B cycle),
#  B -> E -> H, B -> G -> F)
# --------------------------------------------------------------
graph = {
    'A': ['B'],
    'B': ['C', 'D', 'E', 'G'],
    'C': ['B'],
    'D': ['B'],
    'E': ['H'],
    'G': ['F'],
    'H': [],
    'F': []
}

# --------------------------------------------------------------
#  a) Breadth-First Search (BFS) - iterative, similar to example
# --------------------------------------------------------------
def bfs(start):
    visited = []  # List for visited nodes (as in example)
    queue = []    # List as queue (pop(0) as in example)
    levels = {}   # Dict to track levels

    visited.append(start)
    queue.append(start)
    levels[start] = 0

    print("Following is the Breadth-First Search order:")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        # Alphabetical tie-breaking
        for neighbour in sorted(graph.get(node, [])):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                levels[neighbour] = levels[node] + 1

    print("\nLevels (node: level):")
    for node in sorted(levels):
        print(f"  {node}: {levels[node]}")

# --------------------------------------------------------------
#  b) Depth-First Search (DFS) - recursive, similar to example
# --------------------------------------------------------------
visited = []  # Global for recursive (as in example)

def dfs(node, depth=0, levels=None):
    if levels is None:
        levels = {}

    if node in visited:
        return

    visited.append(node)
    print(node, end=" ")
    levels[node] = depth

    # Alphabetical tie-breaking
    for neighbour in sorted(graph.get(node, [])):
        dfs(neighbour, depth + 1, levels)

    return levels

# --------------------------------------------------------------
#  Run both algorithms (starting from 'A')
# --------------------------------------------------------------
if __name__ == "__main__":
    print("=== BFS ===")
    bfs('A')

    print("\n\n=== DFS ===")
    print("Following is the Depth-First Search order:")
    levels_dfs = dfs('A')
    print("\nLevels (node: level):")
    for node in sorted(levels_dfs):
        print(f"  {node}: {levels_dfs[node]}")