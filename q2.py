import streamlit as st
from collections import deque

# ----------------------------
# Graph Definition (Improved)
# ----------------------------
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

# Sort adjacency list alphabetically
for node in graph:
    graph[node] = sorted(graph[node])


# ----------------------------
# BFS FUNCTION (with levels + process path)
# ----------------------------
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    levels = {start_node: 0}
    process_path = []

    while queue:
        node = queue.popleft()
        process_path.append(node)

        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    levels[neighbor] = levels[node] + 1

    return visited, levels, process_path


# ----------------------------
# DFS FUNCTION (with depth + process path)
# ----------------------------
def dfs(graph, node, visited=None, depth_map=None, depth=0, process_path=None):
    if visited is None:
        visited = []
    if depth_map is None:
        depth_map = {}
    if process_path is None:
        process_path = []

    if node not in visited:
        visited.append(node)
        process_path.append(node)
        depth_map[node] = depth

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited, depth_map, depth + 1, process_path)

    return visited, depth_map, process_path


# ----------------------------
# STREAMLIT UI
# ----------------------------
st.title("Graph Search Visualization: BFS & DFS")

# Load graph image
try:
    st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph Structure", use_column_width=True)
except:
    st.warning("LabReport_BSD2513_#1.jpg not found. Please upload it to the same folder or GitHub repo.")

st.write("""
This app demonstrates **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**  
based on the directed graph above.  
All neighbor nodes follow **alphabetical order**.
""")

# Node selection
start_node = st.selectbox("Select a starting node:", sorted(graph.keys()))

if st.button("Run BFS & DFS"):
    # Run BFS & DFS
    bfs_order, bfs_levels, bfs_process = bfs(graph, start_node)
    dfs_order, dfs_depths, dfs_process = dfs(graph, start_node)

    # -------------------
    # BFS Result
    # -------------------
    st.subheader("BFS Result")
    st.write("Order:", " → ".join(bfs_order))
    st.write("Levels:")
    st.table({"Node": bfs_levels.keys(), "Level": bfs_levels.values()})
    st.write("Process Path:")
    st.code(" → ".join(bfs_process))

    # -------------------
    # DFS Result
    # -------------------
    st.subheader("DFS Result")
    st.write("Order:", " → ".join(dfs_order))
    st.write("Depths:")
    st.table({"Node": dfs_depths.keys(), "Depth": dfs_depths.values()})
    st.write("Process Path:")
    st.code(" → ".join(dfs_process))

    # -------------------
    # Comparison
    # -------------------
    st.subheader("Comparison")
    st.write(f"""
    - BFS explores **level by level** starting from {start_node}.  
    - DFS explores **deep into each branch** before backtracking.  
    - Both use **alphabetical tie-breaking** for fair and deterministic traversal.  
    """)

st.markdown("---")
st.caption("Developed for BSD2333 / BSD2513 — Streamlit BFS & DFS App")
