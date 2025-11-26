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
  
    
    if start == goal:
        return [start]
    
    if start not in graph:
        return []
    
    queue = deque([start])
    visited = {start}
    parent = {}
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                
                if neighbor == goal:
                    path = []
                    node = goal
                    while node in parent:
                        path.append(node)
                        node = parent[node]
                    path.append(start)
                    path.reverse()
                    return path
                
                queue.append(neighbor)
    
    return []
