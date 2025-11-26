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
    
    # Edge case: start equals goal
    if start == goal:
        return [start]
    
    # Edge case: start not in graph (no neighbors to explore from)
    if start not in graph:
        return []
    
    # Initialize BFS data structures
    queue = deque([start])  # Queue for BFS traversal
    visited = {start}        # Set of visited nodes
    parent = {}              # Dictionary to track parent of each node for path reconstruction
    
    # BFS traversal - explore level by level
    while queue:
        current = queue.popleft()  # Get next room to explore
        
        # Explore all neighbors of current room
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                # Mark neighbor as visited and record its parent
                visited.add(neighbor)
                parent[neighbor] = current
                
                # Check if we found the goal
                if neighbor == goal:
                    # Reconstruct path by walking backward from goal to start
                    path = []
                    node = goal
                    while node in parent:
                        path.append(node)
                        node = parent[node]
                    path.append(start)
                    path.reverse()  # Reverse to get path from start to goal
                    return path
                
                # Add neighbor to queue for further exploration
                queue.append(neighbor)
    
    # No path found (goal is unreachable or doesn't exist)
    return []
