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
# BFS with Level Tracking
# ----------------------------
def bfs(graph, start_node):
    visited = []
    level_info = []
    queue = deque([(start_node, 0)])  # (node, level)

    while queue:
        node, level = queue.popleft()

        if node not in visited:
            visited.append(node)
            level_info.append((node, level))

            for neighbor in graph[node]:
                queue.append((neighbor, level + 1))

    return level_info


# ----------------------------
# DFS FUNCTION (Recursive)
# ----------------------------
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

    return visited


# ----------------------------
# STREAMLIT UI
# ----------------------------
st.title("Graph Search Visualization: BFS & DFS")

# Load graph image if available
try:
    st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph Structure", use_column_width=True)
except:
    st.warning("LabReport_BSD2513_#1.jpg not found. Please upload it to the same folder or GitHub repo.")

st.write("""
This app demonstrates Breadth-First Search (BFS) and Depth-First Search (DFS) 
based on the directed graph shown above.  
All neighbor nodes are processed in alphabetical order.
""")

# Node selection
start_node = st.selectbox("Select a starting node:", sorted(graph.keys()))

if st.button("Run BFS & DFS"):
    bfs_result = bfs(graph, start_node)
    dfs_result = dfs(graph, start_node)

    # BFS output
    st.subheader("BFS Result (with levels)")
    bfs_formatted = [f"{node} (level {lvl})" for node, lvl in bfs_result]
    st.write(" → ".join(bfs_formatted))

    # DFS output
    st.subheader("DFS Result")
    st.write(" → ".join(dfs_result))

    # Comparison text
    st.subheader("Comparison")
    st.write(f"""
    - BFS explores the graph level by level starting from {start_node}.  
    - DFS explores deeper into paths before backtracking.  
    """)

st.markdown("---")
st.caption("Developed for BSD2333 Data Wrangling — Streamlit Demo App")
