"""
EXPERIMENT 2: Implementation of Breadth First and Depth First Searching Techniques
Course: AI Lab Practical (CSE)
Description:
    Implements Breadth First Search (BFS) and Depth First Search (DFS) algorithms
    on a graph, showing full traversal order and path-finding from Start to Goal node.
"""

from collections import deque


def create_sample_graph():
    """
    Graph representation using Adjacency List:
             A
           /   \
          B     C
         / \   / \
        D   E F   G
             \
              H
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }
    return graph


def breadth_first_search(graph, start_node):
    """
    BFS Traversal using a Queue (FIFO).
    Visits nodes level-by-level.
    """
    visited = []
    queue = deque([start_node])
    visited_set = {start_node}

    while queue:
        current_node = queue.popleft()
        visited.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)

    return visited


def bfs_find_path(graph, start_node, goal_node):
    """
    BFS Path-Finding: Finds the shortest path (fewest edges) from start to goal.
    Stores full paths in the queue.
    """
    queue = deque([[start_node]])
    visited = {start_node}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal_node:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


def depth_first_search(graph, start_node):
    """
    DFS Traversal using a Stack / Iterative method (LIFO).
    Visits along each branch as deep as possible before backtracking.
    """
    visited = []
    visited_set = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited_set:
            visited_set.add(current_node)
            visited.append(current_node)

            # Reverse neighbor list so left-to-right order is preserved when popping
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited_set:
                    stack.append(neighbor)

    return visited


def dfs_find_path(graph, start_node, goal_node, path=None, visited=None):
    """
    DFS Path-Finding (Recursive approach).
    """
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start_node)
    visited.add(start_node)

    if start_node == goal_node:
        return path

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            result_path = dfs_find_path(graph, neighbor, goal_node, list(path), visited.copy())
            if result_path is not None:
                return result_path

    return None


def display_results():
    graph = create_sample_graph()
    start = 'A'
    goal = 'H'

    print("=" * 70)
    print("EXPERIMENT 2: BREADTH FIRST SEARCH (BFS) & DEPTH FIRST SEARCH (DFS)")
    print("=" * 70)
    print("\nGraph Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {', '.join(neighbors)}")

    print("\n" + "-" * 70)
    print("1. BREADTH FIRST SEARCH (BFS):")
    print("-" * 70)
    bfs_traversal = breadth_first_search(graph, start)
    print(f"Starting Node          : {start}")
    print(f"BFS Traversal Order    : {' -> '.join(bfs_traversal)}")

    bfs_path = bfs_find_path(graph, start, goal)
    print(f"Goal Node              : {goal}")
    print(f"BFS Path ({start} to {goal})    : {' -> '.join(bfs_path)} (Length: {len(bfs_path) - 1} edges)")

    print("\n" + "-" * 70)
    print("2. DEPTH FIRST SEARCH (DFS):")
    print("-" * 70)
    dfs_traversal = depth_first_search(graph, start)
    print(f"Starting Node          : {start}")
    print(f"DFS Traversal Order    : {' -> '.join(dfs_traversal)}")

    dfs_path = dfs_find_path(graph, start, goal)
    print(f"Goal Node              : {goal}")
    print(f"DFS Path ({start} to {goal})    : {' -> '.join(dfs_path)} (Length: {len(dfs_path) - 1} edges)")

    print("\n" + "=" * 70)
    print("SUMMARY COMPARISON:")
    print("=" * 70)
    print(f"{'Parameter':<22} | {'BFS':<20} | {'DFS':<20}")
    print("-" * 70)
    print(f"{'Data Structure':<22} | {'Queue (FIFO)':<20} | {'Stack / Recursion':<20}")
    print(f"{'Completeness':<22} | {'Yes (if b is finite)':<20} | {'No (in infinite paths)':<20}")
    print(f"{'Optimality':<22} | {'Yes (unweighted)':<20} | {'No':<20}")
    print(f"{'Time Complexity':<22} | {'O(b^d)':<20} | {'O(b^m)':<20}")
    print(f"{'Space Complexity':<22} | {'O(b^d) [High memory]':<20} | {'O(b*m) [Low memory]':<20}")
    print("=" * 70)


if __name__ == "__main__":
    display_results()
