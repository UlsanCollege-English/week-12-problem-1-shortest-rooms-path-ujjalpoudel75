from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Finds the shortest path between start and goal in a graph using BFS.
    
    Args:
        graph: A dictionary where keys are room names and values are lists of neighboring rooms.
        start: The name of the starting room.
        goal: The name of the target room.
        
    Returns:
        A list of rooms representing the shortest path from start to goal, 
        or an empty list if no path exists or if start/goal are not in the graph.
    """
    # 1. Check if start or goal are in the graph
    if start not in graph or goal not in graph:
        return []
    
    # Edge case: start is the goal
    if start == goal:
        return [start]

    # 2. Initialize BFS structures
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    found = False
    
    # 3. BFS Loop
    while queue:
        current_room = queue.popleft()
        
        if current_room == goal:
            found = True
            break
        
        for neighbor in graph.get(current_room, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_room
                queue.append(neighbor)
    
    # 4. Reconstruct path
    if not found:
        return []
        
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
        
    return path[::-1]
