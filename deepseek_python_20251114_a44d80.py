import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

class GraphSearch:
    def __init__(self):
        # Define the graph from the lab report
        self.graph = {
            'A': ['D', 'C'],
            'B': ['C', 'E'],
            'C': ['B', 'G', 'H'],
            'D': ['A', 'C'],
            'E': ['B', 'G'],
            'F': ['H'],
            'G': ['C', 'E'],
            'H': ['C', 'F']
        }
    
    def bfs(self, start, goal):
        """Breadth-First Search implementation"""
        visited = set()
        queue = deque([[start]])
        
        if start == goal:
            return [start], 0
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            
            if node not in visited:
                neighbours = sorted(self.graph.get(node, []))
                
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    
                    if neighbour == goal:
                        return new_path, len(new_path) - 1
                
                visited.add(node)
        
        return None, float('inf')
    
    def dfs(self, start, goal, path=None, visited=None):
        """Depth-First Search implementation"""
        if path is None:
            path = []
        if visited is None:
            visited = set()
        
        path = path + [start]
        visited.add(start)
        
        if start == goal:
            return path, len(path) - 1
        
        neighbours = sorted(self.graph.get(start, []))
        
        for neighbour in neighbours:
            if neighbour not in visited:
                result_path, cost = self.dfs(neighbour, goal, path, visited)
                if result_path:
                    return result_path, cost
        
        return None, float('inf')
    
    def visualize_graph(self):
        """Visualize the graph using networkx and matplotlib"""
        G = nx.Graph()
        
        for node, neighbours in self.graph.items():
            for neighbour in neighbours:
                G.add_edge(node, neighbour)
        
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=2000, font_size=16, font_weight='bold',
                edge_color='gray', width=2)
        plt.title("Graph Structure for Search Algorithms", fontsize=16)
        return plt

def main():
    st.set_page_config(page_title="AI Search Algorithms", page_icon="🔍", layout="wide")
    
    st.title("🔍 AI Search Algorithms - BFS & DFS")
    st.markdown("**Laboratory Report 1 - BSD3513 Artificial Intelligence**")
    
    # Initialize graph search
    graph_search = GraphSearch()
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the section", 
                                   ["Home", "BFS Algorithm", "DFS Algorithm", "Comparison"])
    
    if app_mode == "Home":
        st.header("Welcome to Search Algorithms Demonstration")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("About This Lab")
            st.markdown("""
            This application demonstrates two fundamental search algorithms:
            - **Breadth-First Search (BFS)**
            - **Depth-First Search (DFS)**
            
            **Graph Structure:**
            - Nodes: A, B, C, D, E, F, G, H
            - Edges are defined in the adjacency list
            """)
            
            st.subheader("Algorithm Complexity")
            st.markdown("""
            | Algorithm | Time Complexity | Space Complexity |
            |-----------|-----------------|------------------|
            | BFS       | O(V + E)        | O(V)             |
            | DFS       | O(V + E)        | O(V)             |
            
            Where V = number of vertices, E = number of edges
            """)
        
        with col2:
            st.subheader("Graph Visualization")
            fig = graph_search.visualize_graph()
            st.pyplot(fig)
    
    elif app_mode == "BFS Algorithm":
        st.header("Breadth-First Search (BFS)")
        
        st.markdown("""
        **BFS Algorithm:**
        - Explores all neighbors at the present depth before moving to nodes at the next depth level
        - Uses queue data structure
        - Guarantees shortest path in unweighted graphs
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_node = st.selectbox("Start Node", sorted(graph_search.graph.keys()), key="bfs_start")
            goal_node = st.selectbox("Goal Node", sorted(graph_search.graph.keys()), key="bfs_goal")
            
            if st.button("Run BFS", key="run_bfs"):
                with st.spinner("Running BFS..."):
                    start_time = time.time()
                    path, cost = graph_search.bfs(start_node, goal_node)
                    end_time = time.time()
                    
                    st.subheader("BFS Results")
                    st.success(f"**Path Found:** {' → '.join(path)}")
                    st.info(f"**Path Cost:** {cost}")
                    st.info(f"**Execution Time:** {(end_time - start_time)*1000:.2f} milliseconds")
                    
                    # Show algorithm steps
                    st.subheader("BFS Process")
                    st.markdown("""
                    **Step-by-step process:**
                    1. Start from the initial node
                    2. Visit all neighbors at current level
                    3. Move to next level neighbors
                    4. Continue until goal is found
                    """)
        
        with col2:
            st.subheader("BFS Visualization")
            fig = graph_search.visualize_graph()
            st.pyplot(fig)
    
    elif app_mode == "DFS Algorithm":
        st.header("Depth-First Search (DFS)")
        
        st.markdown("""
        **DFS Algorithm:**
        - Explores as far as possible along each branch before backtracking
        - Uses stack data structure (recursion)
        - May not find shortest path
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_node = st.selectbox("Start Node", sorted(graph_search.graph.keys()), key="dfs_start")
            goal_node = st.selectbox("Goal Node", sorted(graph_search.graph.keys()), key="dfs_goal")
            
            if st.button("Run DFS", key="run_dfs"):
                with st.spinner("Running DFS..."):
                    start_time = time.time()
                    path, cost = graph_search.dfs(start_node, goal_node)
                    end_time = time.time()
                    
                    st.subheader("DFS Results")
                    if path:
                        st.success(f"**Path Found:** {' → '.join(path)}")
                        st.info(f"**Path Cost:** {cost}")
                    else:
                        st.error("No path found!")
                    st.info(f"**Execution Time:** {(end_time - start_time)*1000:.2f} milliseconds")
                    
                    # Show algorithm steps
                    st.subheader("DFS Process")
                    st.markdown("""
                    **Step-by-step process:**
                    1. Start from the initial node
                    2. Go deep into one branch until dead end
                    3. Backtrack to explore other branches
                    4. Continue until goal is found
                    """)
        
        with col2:
            st.subheader("DFS Visualization")
            fig = graph_search.visualize_graph()
            st.pyplot(fig)
    
    elif app_mode == "Comparison":
        st.header("BFS vs DFS Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Breadth-First Search")
            st.markdown("""
            **Advantages:**
            - ✅ Guarantees shortest path
            - ✅ Complete (always finds solution if exists)
            - ✅ Optimal for unweighted graphs
            
            **Disadvantages:**
            - ❌ High memory usage
            - ❌ Slower for deep graphs
            
            **Use Cases:**
            - Shortest path finding
            - Web crawling
            - Social network analysis
            """)
        
        with col2:
            st.subheader("Depth-First Search")
            st.markdown("""
            **Advantages:**
            - ✅ Low memory usage
            - ✅ Faster for deep graphs
            - ✅ Good for cycle detection
            
            **Disadvantages:**
            - ❌ No shortest path guarantee
            - ❌ May get stuck in infinite depth
            - ❌ Not complete for infinite graphs
            
            **Use Cases:**
            - Maze solving
            - Topological sorting
            - Path existence checking
            """)
        
        # Performance comparison
        st.subheader("Performance Comparison")
        
        test_cases = [
            ("A", "G"),
            ("D", "F"),
            ("B", "H")
        ]
        
        results = []
        for start, goal in test_cases:
            # BFS
            bfs_start = time.time()
            bfs_path, bfs_cost = graph_search.bfs(start, goal)
            bfs_time = (time.time() - bfs_start) * 1000
            
            # DFS
            dfs_start = time.time()
            dfs_path, dfs_cost = graph_search.dfs(start, goal)
            dfs_time = (time.time() - dfs_start) * 1000
            
            results.append({
                "Start": start,
                "Goal": goal,
                "BFS Path": " → ".join(bfs_path) if bfs_path else "No path",
                "BFS Cost": bfs_cost,
                "BFS Time (ms)": f"{bfs_time:.2f}",
                "DFS Path": " → ".join(dfs_path) if dfs_path else "No path",
                "DFS Cost": dfs_cost,
                "DFS Time (ms)": f"{dfs_time:.2f}"
            })
        
        # Display results as table
        st.table(results)

    # Footer
    st.markdown("---")
    st.markdown("**Laboratory Report 1 - BSD3513 Artificial Intelligence**")
    st.markdown("**Search Algorithms Implementation - BFS & DFS**")

if __name__ == "__main__":
    main()