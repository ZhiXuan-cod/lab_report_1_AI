import streamlit as st

# --------------------------------------------------------------
#  Graph definition (based on the directed graph)
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
#  a) Breadth-First Search (BFS)
# --------------------------------------------------------------
def bfs(start):
    visited = []
    queue = []
    levels = {}

    visited.append(start)
    queue.append(start)
    levels[start] = 0

    expansion_order = [start]  # Track order of expansion

    while queue:
        node = queue.pop(0)
        # Find neighbors to expand (alphabetical)
        for neighbour in sorted(graph.get(node, [])):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                levels[neighbour] = levels[node] + 1
                expansion_order.append(neighbour)  # Wait, no: expansion is when dequeued

    # Correct expansion order: when dequeued/printed
    # Reset to simulate
    visited = [start]
    queue = [start]
    expansion_order = []
    levels = {start: 0}

    while queue:
        node = queue.pop(0)
        expansion_order.append(node)
        for neighbour in sorted(graph.get(node, [])):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                levels[neighbour] = levels[node] + 1

    return expansion_order, levels

# --------------------------------------------------------------
#  b) Depth-First Search (DFS) - recursive
# --------------------------------------------------------------
def dfs_recursive(node, visited, levels, expansion_order):
    if node in visited:
        return
    visited.add(node)
    expansion_order.append(node)
    levels[node] = levels.get(node, 0) + 1 if expansion_order else 0  # Wait, fix depth

# Better: use depth param
def dfs(start):
    visited = set()
    expansion_order = []
    levels = {start: 0}

    def recurse(node, depth):
        if node in visited:
            return
        visited.add(node)
        expansion_order.append(node)
        levels[node] = depth

        # Alphabetical tie-breaking
        for neighbour in sorted(graph.get(node, [])):
            recurse(neighbour, depth + 1)

    recurse(start, 0)
    return expansion_order, levels

# --------------------------------------------------------------
#  Streamlit UI
# --------------------------------------------------------------
st.title("Graph Search Algorithms: BFS vs DFS")
st.write("Explore Breadth-First Search (BFS) and Depth-First Search (DFS) on the directed graph, with alphabetical tie-breaking for node expansion. Start from node **A**.")

# Sidebar for controls
st.sidebar.header("Options")
run_bfs = st.sidebar.checkbox("Run BFS", value=True)
run_dfs = st.sidebar.checkbox("Run DFS", value=True)
start_node = st.sidebar.text_input("Start Node", value="A", help="Default is A")

if st.sidebar.button("Run Searches"):
    if run_bfs:
        with st.container():
            st.subheader("Breadth-First Search (BFS)")
            bfs_order, bfs_levels = bfs(start_node)
            st.success(f"**Expansion Order:** {' -> '.join(bfs_order)}")
            st.info("**Process Path:** Queue-based, level-by-level. Neighbors enqueued in alphabetical order (e.g., from B: C, D, E, G).")
            
            # Levels table
            levels_data = {"Node": list(bfs_levels.keys()), "Level": list(bfs_levels.values())}
            st.table(levels_data)

    if run_dfs:
        with st.container():
            st.subheader("Depth-First Search (DFS)")
            dfs_order, dfs_levels = dfs(start_node)
            st.success(f"**Expansion Order:** {' -> '.join(dfs_order)}")
            st.info("**Process Path:** Recursive, depth-first. Neighbors recursed in alphabetical order (e.g., from B: dive into C first, then backtrack).")
            
            # Levels table
            levels_data = {"Node": list(dfs_levels.keys()), "Level": list(dfs_levels.values())}
            st.table(levels_data)

# Comparison Table (always shown)
st.subheader("Level Comparison: BFS vs DFS")
comparison_data = {
    "Node": ["A", "B", "C", "D", "E", "G", "H", "F"],
    "BFS Level": [0, 1, 2, 2, 2, 2, 3, 3],
    "DFS Level": [0, 1, 2, 2, 2, 2, 3, 3],
    "Notes": [
        "Start node",
        "Direct from A",
        "First alpha from B (C < D)",
        "Next from B",
        "Next from B",
        "Last from B",
        "From E",
        "From G"
    ]
}
st.table(comparison_data)

st.write("---")
st.caption("Graph: A→B→{C↺B, D↺B, E→H, G→F} | Built with ❤️ using Streamlit")