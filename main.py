from collections import deque


def bfs_shortest_path(graph, start, goal):
    """
    Find the shortest path from start to goal using BFS.
    
    Args:
        graph: dict mapping room -> list of neighboring rooms
        start: starting room name (string)
        goal: target room name (string)
    
    Returns:
        List of rooms from start to goal (shortest path), or [] if no path exists
    """
    
    # Step 1: Read & Understand
    # We need to find the shortest path between two nodes in an unweighted graph
    # using Breadth-First Search (BFS).
    
    # Step 2: Re-phrase
    # "Find a path with the fewest edges from start to goal using layer-by-layer search."
    
    # Step 3: Identify Input / Output / Variables
    # Inputs: graph (dict), start (string), goal (string)
    # Output: path (list of strings)
    # Main data structures: queue (deque), visited (set), parent (dict)
    
    # Step 4: Break Down the Problem
    # - Use a queue to explore rooms level by level
    # - Mark rooms as visited to avoid cycles
    # - Track parent relationships to reconstruct the path
    # - Handle edge cases: start == goal, missing nodes, disconnected graph
    
    # Step 5: Pseudocode
    # 1. Check if start or goal is not in graph -> return []
    # 2. If start == goal -> return [start]
    # 3. Initialize queue with start, visited set, and parent dict
    # 4. While queue is not empty:
    #    - Dequeue current room
    #    - For each neighbor:
    #      - If not visited and in graph:
    #        - Mark as visited
    #        - Record parent
    #        - Enqueue neighbor
    #        - If neighbor is goal, reconstruct path and return
    # 5. If goal not reached, return []
    
    # Step 6: Write the Code
    
    # Edge case: start or goal not in graph
    if start not in graph or goal not in graph:
        return []
    
    # Edge case: start equals goal
    if start == goal:
        return [start]
    
    # Initialize BFS data structures
    queue = deque([start])
    visited = {start}
    parent = {}
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Explore all neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                
                # Found the goal
                if neighbor == goal:
                    # Reconstruct path by walking backward from goal to start
                    path = []
                    node = goal
                    while node != start:
                        path.append(node)
                        node = parent[node]
                    path.append(start)
                    path.reverse()
                    return path
                
                queue.append(neighbor)
    
    # No path found
    return []

