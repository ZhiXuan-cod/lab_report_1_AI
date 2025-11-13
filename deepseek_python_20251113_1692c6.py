import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Function for BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # (node, path)
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in sorted(graph[node]):  # Alphabetical tie-breaking
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Function for DFS
def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]  # (node, path)
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            # Add neighbors in reverse alphabetical order for correct DFS with stack
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# Streamlit UI
st.title("BFS & DFS Pathfinding Visualizer")
st.write("""
This app demonstrates Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms on a user-defined graph.
Enter your graph structure below.
""")

# ... (Code for graph input, algorithm selection, and visualization would go here) ...

# Example usage after getting user input
if st.button('Find Path'):
    if algorithm == 'BFS':
        path = bfs(user_graph, start_node, goal_node)
    else:
        path = dfs(user_graph, start_node, goal_node)

    if path:
        st.success(f"Path found: {' -> '.join(path)}")
        # ... Code to visualize the graph and highlight the path ...
    else:
        st.error("No path found!")
        
st.markdown("### Complexity Analysis")
st.write("**Time Complexity:** O(V + E) - where V is the number of vertices (nodes) and E is the number of edges. We potentially visit every node and edge once.")
st.write("**Space Complexity:** O(V) - for storing the visited set and the queue/stack in the worst case.")