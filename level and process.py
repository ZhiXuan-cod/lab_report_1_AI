import streamlit as st
from collections import deque

# ==============================================
# Improved Graph (Alphabetically Sorted)
# ==============================================
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


# ==============================================
# BFS with LEVEL Tracking and CLEAR PROCESS PATH
# ==============================================
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


# ==============================================
# DFS with DEPTH Tracking and CLEAR PROCESS PATH
# ==============================================
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


# ==============================================
# STREAMLIT UI
# ==============================================
st.title("Graph Search Visualization: BFS & DFS")

# Display Graph Image from GitHub Repo
try:
    st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph Structure", use_column_width=True)
except:
    st.warning("Graph image not found. Please upload 'LabReport_BSD2513_#1.jpg' to the repo.")

st.write("""
This Streamlit app demonstrates **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**  
on the directed graph shown above.  
All node expansions use **alphabetical tie-breaking**.
""")

# Node selection
start_node = st.selectbox("Select the START node:", sorted(graph.keys()), index=0)

if st.button("Run BFS & DFS"):
    # ---------- BFS ----------
    bfs_order, bfs_levels, bfs_process = bfs_with_details(graph, start_node)

    st.subheader("BFS — Breadth-First Search (Level-by-Level)")
    st.write("**Expansion Order:**")
    st.success(" → ".join(bfs_order))

    st.write("**BFS Levels (Shortest Distance from Start):**")
    st.table({"Node": bfs_levels.keys(), "Level": bfs_levels.values()})

    st.info("""
    **BFS Process Path Explanation:**  
    - BFS explores the graph **level-by-level**.  
    - First it visits all nodes at Level 0, then Level 1, then Level 2, etc.  
    - The queue ensures the search expands outward like ripples in water.  
    - Alphabetical order determines which neighbor enters the queue first.
    """)

    st.write("**Actual Node Processing Path (Queue Sequence):**")
    st.code(" → ".join(bfs_process))


    # ---------- DFS ----------
    dfs_order, dfs_depths, dfs_process = dfs_with_details(graph, start_node)

    st.subheader("DFS — Depth-First Search (Deep Path First)")
    st.write("**Expansion Order:**")
    st.success(" → ".join(dfs_order))

    st.write("**DFS Depths (How Deep Each Node Was First Reached):**")
    st.table({"Node": dfs_depths.keys(), "Depth": dfs_depths.values()})

    st.info("""
    **DFS Process Path Explanation:**  
    - DFS goes **as deep as possible** into one path before backtracking.  
    - It follows the first alphabetical neighbor, explores fully,  
      then returns and explores the next branch.  
    - This creates a long chain-like exploration pattern.
    """)

    st.write("**Actual Node Processing Path (Recursive Visit Order):**")
    st.code(" → ".join(dfs_process))


    # ---------- Comparison ----------
    st.subheader("🔍 BFS vs DFS — Summary Comparison")
    st.write(f"""
    **Starting Node:** {start_node}

    - **BFS** focuses on *levels* and always produces the shortest path tree.  
    - **DFS** focuses on *deep exploration*, following one full path first.  
    - BFS processes nodes in horizontal layers,  
      while DFS processes nodes in vertical depth-first chains.
    """)

st.markdown("---")
st.caption("Developed for BSD2513 / BSD2333 — Streamlit BFS & DFS Visualization Tool")
