from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Finds the shortest path between two nodes in a graph using Breadth-First Search.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes and values are lists of neighbors.
        start (str): The starting node.
        goal (str): The goal node.

    Returns:
        list: A list representing the shortest path from start to goal, or an empty list if no path exists or if start/goal are not in the graph.
    """

    # 1. Read & Understand:
    # Find the shortest sequence of rooms (nodes) from a start room to a target room in a museum (graph).

    # 2. Re-phrase:
    # Find a path with the fewest edges from start to goal.

    # 3. Identify Input / Output / Variables:
    # Inputs: graph, start, goal
    # Output: path list
    # Main data structures: queue, visited, parent

    # 4. Break Down the Problem:
    # - Pick the next room using a queue (FIFO).
    # - Avoid visiting rooms twice using a set.
    # - Remember the path using a parent dictionary.

    # 5. Pseudocode:
    # - If start or goal not in graph, return [].
    # - Initialize queue with start.
    # - Initialize visited set with start.
    # - Initialize parent dictionary.
    # - While queue is not empty:
    #   - Dequeue a node.
    #   - If node is the goal, reconstruct and return the path.
    #   - For each neighbor of the node:
    #     - If neighbor not in visited:
    #       - Add neighbor to visited.
    #       - Enqueue neighbor.
    #       - Set parent of neighbor to node.
    # - If goal not reached, return [].

    # 6. Write the Code:
    if start not in graph or goal not in graph:
        return []

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        node = queue.popleft()

        if node == goal:
            # Reconstruct path
            path = []
            while node is not None:
                path.append(node)
                node = parent.get(node)
            return path[::-1]  # Reverse the path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node

    # 7. Debug & 8. Optimize:
    return []