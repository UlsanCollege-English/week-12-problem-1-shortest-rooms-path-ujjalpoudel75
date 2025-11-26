from collections import deque

def bfs_shortest_path(graph, start, goal):
    # ==========================================
    # Step 1: Read & Understand
    # We need to find the shortest path between two rooms in a museum.
    # Since edges are unweighted, BFS is the correct algorithm.

    # Step 2: Re-phrase
    # Find a list of nodes connecting 'start' to 'goal' with the minimum number of edges.

    # Step 3: Identify Input / Output / Variables
    # Input: graph (dict), start (str), goal (str)
    # Output: list of strings (path) or []
    # Variables: queue (for BFS), visited (set), parent (dict)

    # Step 4: Break Down the Problem
    # 1. Check edge cases (start/goal missing, start==goal).
    # 2. Loop with a queue.
    # 3. Track parents to rebuild the path later.

    # Step 5: Pseudocode
    # If start/goal not in graph -> return []
    # If start == goal -> return [start]
    # Queue = [start], Visited = {start}, Parent = {start: None}
    # While Queue not empty:
    #   Curr = pop()
    #   If Curr == Goal -> Stop
    #   For neighbor in graph[Curr]:
    #     If not visited -> Add to Queue, Mark Visited, Record Parent
    # Rebuild path from Goal back to Start using Parent dict.
    # ==========================================

    # Step 6: Write the Code

    # Edge Case: Start or Goal does not exist in the graph
    if start not in graph or goal not in graph:
        return []

    # Edge Case: Start is the Goal
    if start == goal:
        return [start]

    # Initialize BFS structures
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    found = False

    # Standard BFS Loop
    while queue:
        current_room = queue.popleft()

        if current_room == goal:
            found = True
            break

        # Check neighbors
        # We use .get() just in case a neighbor listed isn't a key in the dict
        for neighbor in graph.get(current_room, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_room
                queue.append(neighbor)

    # Step 7: Debug / Step 8: Optimize
    # Reconstruct path by backtracking from goal to start
    if found:
        path = []
        curr = goal
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        return path[::-1] # Reverse to get Start -> Goal
    else:
        return []