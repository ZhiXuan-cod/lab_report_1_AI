import streamlit as st
from collections import deque

# ================================
# Graph (Alphabetically Sorted)
# ================================
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

# Sort adjacency lists alphabetically
for node in graph:
    graph[node] = sorted(graph[node])


# ================================
# BFS (Level + Process Path)
# ================================
def bfs_with_details(graph, start):
    visited = []
    queue = deque([start])
    levels = {start: 0}
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


# ================================
# DFS (Depth + Process Path)
# ================================
def dfs_with_details(graph, start):
    visited = []
    process_path = []
    depth_map = {start: 0}

    def dfs_recursive(node, depth):
        if node not in visited:
            visited.append(node)
            process_path.append(node)
            depth_map[node] = depth

            for neighbor in graph[node]:
                dfs_recursive(neighbor, depth + 1)

    dfs_recursive(start, 0)
    return visited, depth_map, process_path


# ================================
# Streamlit UI
# ================================
st.title("BFS & DFS Traversal Visualization")

# Graph Image Loading (Put Your Image in Same Folder or GitHub Repo)
try:
    st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph", use_column_width=True)
except:
    st.warning("Image not found. Please upload 'LabReport_BSD2513_#1.jpg' to the project folder or GitHub repo.")


start_node = st.selectbox("Select START Node:", sorted(graph.keys()))

if st.button("Run Search"):
    bfs_order, bfs_levels, bfs_process = bfs_with_details(graph, start_node)
    dfs_order, dfs_depths, dfs_process = dfs_with_details(graph, start_node)

    # ================================
    # BFS OUTPUT
    # ================================
    st.subheader("Breadth-First Search (BFS)")
    st.write("Order:", " → ".join(bfs_order))
    st.write("Levels:")
    st.table({"Node": bfs_levels.keys(), "Level": bfs_levels.values()})
    st.write("Process Path:")
    st.code(" → ".join(bfs_process))

    # ================================
    # DFS OUTPUT
    # ================================
    st.subheader("Depth-First Search (DFS)")
    st.write("Order:", " → ".join(dfs_order))
    st.write("Depths:")
    st.table({"Node": dfs_depths.keys(), "Depth": dfs_depths.values()})
    st.write("Process Path:")
    st.code(" → ".join(dfs_process))

    # ================================
    # Comparison
    # ================================
    st.subheader("Comparison")
    st.write(f"""
    **Starting Node:** {start_node}

    - BFS explores level-by-level.
    - DFS dives deep into each path before backtracking.
    - Alphabetical tie-breaking is applied in both searches.
    """)

