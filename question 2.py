import streamlit as st

# --------------------------------------------------------------
# CORRECT GRAPH BASED ON THE IMAGE
# --------------------------------------------------------------
# Edges interpreted directly from the diagram
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F'],
    'H': ['F', 'G'],
    'F': []
}

# --------------------------------------------------------------
# Breadth-First Search (BFS)
# --------------------------------------------------------------
def bfs(start):
    visited = []
    queue = []
    level = {start: 0}
    expansion = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        expansion.append(node)

        for neighbour in sorted(graph.get(node, [])):  # Alphabetical
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                level[neighbour] = level[node] + 1

    return expansion, level

# --------------------------------------------------------------
# Depth-First Search (DFS) using RECURSION
# --------------------------------------------------------------
def dfs(start):
    visited = set()
    expansion = []
    level = {}

    def recurse(node, depth):
        if node in visited:
            return
        visited.add(node)
        expansion.append(node)
        level[node] = depth

        for neighbour in sorted(graph.get(node, [])):  # Alphabetical
            recurse(neighbour, depth + 1)

    recurse(start, 0)
    return expansion, level

# --------------------------------------------------------------
# Streamlit UI
# --------------------------------------------------------------
st.title("Graph Search Algorithms: BFS vs DFS")
st.write("This app performs **BFS** and **DFS** on the directed graph (with alphabetical tie-breaking).")

# Sidebar
st.sidebar.header("Controls")
start_node = st.sidebar.text_input("Start Node", value="A").upper()
run_bfs = st.sidebar.checkbox("Run BFS", value=True)
run_dfs = st.sidebar.checkbox("Run DFS", value=True)

if st.sidebar.button("Run Search"):

    # ----------------------------------------------------------
    # BFS
    # ----------------------------------------------------------
    if run_bfs:
        st.subheader("Breadth-First Search (BFS)")
        bfs_order, bfs_level = bfs(start_node)

        st.success("Expansion Order: " + " → ".join(bfs_order))
        st.info("Process Path: Level-by-level expansion using a queue. Alphabetical neighbor ordering.")

        st.write("### BFS Levels")
        st.table({"Node": list(bfs_level.keys()), "Level": list(bfs_level.values())})

    # ----------------------------------------------------------
    # DFS
    # ----------------------------------------------------------
    if run_dfs:
        st.subheader("Depth-First Search (DFS)")
        dfs_order, dfs_level = dfs(start_node)

        st.success("Expansion Order: " + " → ".join(dfs_order))
        st.info("Process Path: Recursive depth-first expansion. Alphabetical neighbor ordering.")

        st.write("### DFS Levels")
        st.table({"Node": list(dfs_level.keys()), "Level": list(dfs_level.values())})

# --------------------------------------------------------------
# Always show comparison table (blank at first)
# --------------------------------------------------------------
st.write("---")
st.subheader("Adjacency List (Graph from Image)")
st.json(graph)

st.caption("Alphabetical tie-breaking is applied when choosing between multiple neighbors.")
