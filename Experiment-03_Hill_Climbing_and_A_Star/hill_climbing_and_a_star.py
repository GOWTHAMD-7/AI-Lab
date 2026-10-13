"""
EXPERIMENT 3: Implementation of Hill Climbing Algorithm and A* Algorithm
Course: AI Lab Practical (CSE)
Description:
    Part A: Hill Climbing local search algorithm for state space optimization.
    Part B: A* (A-Star) heuristic search algorithm with evaluation function f(n) = g(n) + h(n).
"""

import heapq


# ======================================================================
# PART A: HILL CLIMBING ALGORITHM
# ======================================================================
def objective_function(x):
    """
    Objective function to maximize: f(x) = -(x - 6)^2 + 40
    Has a peak / maximum at x = 6 where f(6) = 40.
    """
    return -(x - 6) ** 2 + 40


def hill_climbing(start_x, step_size=1, min_x=0, max_x=12):
    """
    Hill Climbing Algorithm:
    At each step, examines neighbors (x - step_size, x + step_size)
    and moves to the neighbor with a strictly higher objective score.
    Stops when no neighbor has a higher score (local/global peak).
    """
    current_x = start_x
    current_score = objective_function(current_x)
    trajectory = [(current_x, current_score)]

    print(f"Starting Hill Climbing from x = {current_x}, Score f(x) = {current_score}")

    step_count = 0
    while True:
        step_count += 1
        # Generate possible neighbors within bounds
        neighbors = []
        if current_x - step_size >= min_x:
            neighbors.append(current_x - step_size)
        if current_x + step_size <= max_x:
            neighbors.append(current_x + step_size)

        # Evaluate neighbors
        best_neighbor = None
        best_neighbor_score = current_score

        for neighbor in neighbors:
            score = objective_function(neighbor)
            if score > best_neighbor_score:
                best_neighbor_score = score
                best_neighbor = neighbor

        # Check termination condition: no neighbor is better than current state
        if best_neighbor is None or best_neighbor_score <= current_score:
            print(f"Peak reached at Step {step_count}: No neighboring state has a higher value.")
            break

        # Move uphill
        current_x = best_neighbor
        current_score = best_neighbor_score
        trajectory.append((current_x, current_score))
        print(f"  Step {step_count}: Moved to x = {current_x}, Score f(x) = {current_score}")

    return current_x, current_score, trajectory


# ======================================================================
# PART B: A* (A-STAR) ALGORITHM
# ======================================================================
class AStarSearch:
    def __init__(self, graph, heuristics):
        """
        graph: Dict mapping node -> list of tuples (neighbor, edge_cost)
        heuristics: Dict mapping node -> estimated cost to goal h(n)
        """
        self.graph = graph
        self.heuristics = heuristics

    def search(self, start, goal):
        """
        A* Search implementation:
        Maintains priority queue of tuples: (f_cost, g_cost, current_node, path)
        where f(n) = g(n) + h(n).
        """
        # Priority queue stores: (f_score, g_score, node, path)
        initial_h = self.heuristics.get(start, 0)
        open_list = [(initial_h, 0, start, [start])]
        visited_best_g = {}

        step = 0
        print(f"\nTracing A* Search from '{start}' to '{goal}':")
        print(f"{'Step':<6} | {'Current':<8} | {'g(n)':<6} | {'h(n)':<6} | {'f(n)':<6} | {'Path':<20}")
        print("-" * 65)

        while open_list:
            f_score, g_score, current_node, path = heapq.heappop(open_list)
            step += 1
            h_score = self.heuristics.get(current_node, 0)

            path_str = "->".join(path)
            print(f"{step:<6} | {current_node:<8} | {g_score:<6} | {h_score:<6} | {f_score:<6} | {path_str:<20}")

            # Goal test
            if current_node == goal:
                return path, g_score

            # Skip if we already reached this node with an equal or lower cost
            if current_node in visited_best_g and visited_best_g[current_node] <= g_score:
                continue
            visited_best_g[current_node] = g_score

            # Expand neighbors
            for neighbor, weight in self.graph.get(current_node, []):
                new_g = g_score + weight
                new_h = self.heuristics.get(neighbor, 0)
                new_f = new_g + new_h
                new_path = path + [neighbor]

                if neighbor not in visited_best_g or visited_best_g[neighbor] > new_g:
                    heapq.heappush(open_list, (new_f, new_g, neighbor, new_path))

        return None, float('inf')


def run_experiment():
    print("=" * 70)
    print("EXPERIMENT 3: HILL CLIMBING AND A* ALGORITHMS")
    print("=" * 70)

    # 1. HILL CLIMBING EXECUTION
    print("\n" + "=" * 70)
    print("PART A: HILL CLIMBING ALGORITHM")
    print("=" * 70)
    print("Objective: Maximize f(x) = -(x - 6)^2 + 40, Range: [0, 12]")
    initial_position = 1
    best_x, max_val, path = hill_climbing(start_x=initial_position, step_size=1)
    print(f"\nHill Climbing Result:")
    print(f"  Optimal State Found : x = {best_x}")
    print(f"  Maximum Value       : f({best_x}) = {max_val}")
    print(f"  Traversal Path      : {' -> '.join([f'x={x}({v})' for x, v in path])}")

    # 2. A* SEARCH EXECUTION
    print("\n" + "=" * 70)
    print("PART B: A* (A-STAR) ALGORITHM")
    print("=" * 70)

    # Graph with edge weights g(n, m)
    graph = {
        'S': [('A', 1), ('G', 10)],
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 5)],
        'C': [('D', 3), ('G', 4)],
        'D': [('G', 2)],
        'G': []
    }

    # Heuristic estimates h(n) to Goal 'G'
    heuristics = {
        'S': 5,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 6,
        'G': 0
    }

    print("Graph Edge Costs g(n):")
    for node, edges in graph.items():
        edge_info = [f"{dest}(cost={cost})" for dest, cost in edges]
        print(f"  {node} -> {', '.join(edge_info) if edge_info else 'None (Goal)'}")

    print("\nHeuristic Values h(n) to Goal 'G':")
    for node, h_val in heuristics.items():
        print(f"  h({node}) = {h_val}")

    astar = AStarSearch(graph, heuristics)
    optimal_path, total_cost = astar.search(start='S', goal='G')

    print("-" * 65)
    print(f"A* Search Result:")
    print(f"  Optimal Path : {' -> '.join(optimal_path)}")
    print(f"  Total Cost   : {total_cost}")
    print("=" * 70)


if __name__ == "__main__":
    run_experiment()
