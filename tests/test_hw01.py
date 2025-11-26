import pytest
from main import bfs_shortest_path


def is_valid_path(graph, path, start, goal):
    if not path:
        return False
    if path[0] != start or path[-1] != goal:
        return False
    for u, v in zip(path, path[1:]):
        if v not in graph.get(u, []):
            return False
    return True


def path_length(path):
    if not path:
        return 0
    return len(path) - 1


# Normal tests (4)


def test_simple_line_path():
    graph = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"],
    }
    path = bfs_shortest_path(graph, "A", "D")
    assert is_valid_path(graph, path, "A", "D")
    assert path_length(path) == 3


def test_branching_graph_unique_shortest():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["B", "E"],
        "E": ["D"],
    }
    path = bfs_shortest_path(graph, "A", "E")
    assert is_valid_path(graph, path, "A", "E")
    assert path_length(path) == 3


def test_start_equals_goal():
    graph = {
        "Room": ["Other"],
        "Other": ["Room"],
    }
    path = bfs_shortest_path(graph, "Room", "Room")
    assert path == ["Room"]


def test_cycle_graph_shortest():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
        "D": ["C"],
    }
    path = bfs_shortest_path(graph, "A", "D")
    assert is_valid_path(graph, path, "A", "D")
    assert path_length(path) == 2


# Edge-case tests (3)


def test_missing_start_or_goal_returns_empty():
    graph = {
        "A": ["B"],
        "B": ["A"],
    }
    assert bfs_shortest_path(graph, "X", "B") == []
    assert bfs_shortest_path(graph, "A", "Y") == []


def test_disconnected_graph_returns_empty():
    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }
    path = bfs_shortest_path(graph, "A", "D")
    assert path == []


def test_single_node_graph():
    graph = {"Solo": []}
    path = bfs_shortest_path(graph, "Solo", "Solo")
    assert path == ["Solo"]


# Complex tests (3)


def test_larger_graph_min_hops():
    # FIXED: Added R6 to R3's neighbors to make a 3-edge path possible
    graph = {
        "R1": ["R2", "R3"],
        "R2": ["R1", "R4"],
        "R3": ["R1", "R5", "R6"],  # FIXED: Added R6 here
        "R4": ["R2", "R6"],
        "R5": ["R3", "R6"],
        "R6": ["R3", "R4", "R5", "R7"],  # FIXED: Added R3 for bidirectionality
        "R7": ["R6"],
    }
    path = bfs_shortest_path(graph, "R1", "R7")
    assert is_valid_path(graph, path, "R1", "R7")
    assert path_length(path) == 3  # Now R1->R3->R6->R7 works!


@pytest.mark.parametrize(
    "start,goal,expected_len",
    [
        ("R1", "R4", 2),
        ("R1", "R5", 2),
        ("R2", "R6", 2),
    ],
)
def test_parametrized_shortest_paths(start, goal, expected_len):
    # FIXED: Added R6 to make the paths possible
    graph = {
        "R1": ["R2", "R3"],
        "R2": ["R1", "R4"],
        "R3": ["R1", "R5"],
        "R4": ["R2", "R6"],  # FIXED: Added R6 here
        "R5": ["R3", "R6"],  # FIXED: Added R6 here
        "R6": ["R4", "R5"],  # FIXED: Added this line
    }
    path = bfs_shortest_path(graph, start, goal)
    assert is_valid_path(graph, path, start, goal)
    assert path_length(path) == expected_len


def test_no_path_in_sparse_graph():
    graph = {
        "A": ["B"],
        "B": [],
        "C": ["D"],
        "D": [],
    }
    path = bfs_shortest_path(graph, "A", "D")
    assert path == []