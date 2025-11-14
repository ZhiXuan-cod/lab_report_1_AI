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

# Sort adjacency list alphabetically for consistent BFS/DFS
for node in graph:
    graph[node] = sorted(graph[node])


# ----------------------------
# BFS FUNCTION
# ----------------------------
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited


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
This app demonstrates **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** 
based on the directed graph shown above.  
All neighbor nodes are processed in **alphabetical order** for fairness.
""")

# Node selection
start_node = st.selectbox("Select a starting node:", sorted(graph.keys()))

if st.button("Run BFS & DFS"):
    bfs_result = bfs(graph, start_node)
    dfs_result = dfs(graph, start_node)

    st.subheader("BFS Result")
    st.write(" → ".join(bfs_result))

    st.subheader("DFS Result")
    st.write(" → ".join(dfs_result))

    # Comparison
    st.subheader("Comparison")
    st.write(f"""
    - BFS explores **level by level** starting from {start_node}.  
    - DFS explores **deep into the path** before backtracking.  
    """)

st.markdown("---")
st.caption("Developed for BSD2333 Data Wrangling — Streamlit Demo App")
