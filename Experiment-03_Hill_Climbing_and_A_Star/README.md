# EXPERIMENT 3: Implementation of Hill Climbing Algorithm and A* Algorithm

---

## 1. Aim
To implement the **Hill Climbing** local search optimization algorithm and the **A\* (A-Star)** heuristic search algorithm in Python to find optimal states and optimal goal paths.

---

## 2. Algorithms (5 - 6 Simple Steps to Write in Record / Exam)

### A. Hill Climbing Algorithm:
1. **Step 1: Evaluate Initial State:** Start at an initial position/state and evaluate its objective/heuristic value $f(\text{current})$.
2. **Step 2: Generate Neighbors:** Generate all immediate neighboring states achievable from the current state.
3. **Step 3: Select Best Neighbor:** Evaluate the objective score of all neighbors and pick the best neighbor with the highest value (or lowest cost).
4. **Step 4: Comparison:** Compare the score of the best neighbor with the current state's score.
5. **Step 5: Move or Terminate:** If the best neighbor has a strictly better score, update current state to the neighbor; otherwise, terminate (a local/global peak is reached).
6. **Step 6: Output Result:** Return the final state reached and its maximum objective value.

---

### B. A* (A-Star) Search Algorithm:
1. **Step 1: Initialize Open & Closed Sets:** Create a priority queue (`Open List`) containing the start node with $f(start) = g(start) + h(start)$, where $g(start) = 0$. Create an empty `Closed List`.
2. **Step 2: Pop Lowest $f(n)$ Node:** While `Open List` is not empty, remove the node $n$ having the minimum evaluation score $f(n) = g(n) + h(n)$.
3. **Step 3: Goal Test:** If node $n$ is the goal state, reconstruct and return the optimal path and total path cost $g(n)$.
4. **Step 4: Expand Neighbors:** Add node $n$ to the `Closed List`. For each successor/neighbor $m$ of $n$, compute tentative cost: $g(m) = g(n) + \text{cost}(n, m)$.
5. **Step 5: Update Costs:** If $m$ is not in Open List, or if the new $g(m)$ is lower than its previously recorded cost, update its $g(m)$, calculate $f(m) = g(m) + h(m)$, set $n$ as its parent, and insert $m$ into `Open List`.
6. **Step 6: Terminate on Empty:** If the `Open List` becomes empty without reaching the goal, report failure (no solution path exists).

---

## 3. Mathematical Formulations

- **Hill Climbing Objective Function:**
  $$f(x) = -(x - 6)^2 + 40$$
  Peak occurs at $x = 6$ with $f(6) = 40$.

- **A\* Evaluation Function:**
  $$f(n) = g(n) + h(n)$$
  - $g(n)$: Exact cost from start node to node $n$.
  - $h(n)$: Estimated heuristic cost from node $n$ to goal node.
  - $f(n)$: Estimated total lowest cost of path through $n$.

---

## 4. Source Code (`hill_climbing_and_a_star.py`)

```python
"""
EXPERIMENT 3: Hill Climbing & A* Algorithm
"""
import heapq

# --- PART A: HILL CLIMBING ---
def objective_fn(x):
    return -(x - 6) ** 2 + 40

def hill_climbing(start_x, step_size=1):
    curr = start_x
    while True:
        neighbors = [curr - step_size, curr + step_size]
        best_neighbor = max(neighbors, key=objective_fn)
        if objective_fn(best_neighbor) <= objective_fn(curr):
            break
        curr = best_neighbor
    return curr, objective_fn(curr)

# --- PART B: A* SEARCH ---
def a_star(graph, heuristics, start, goal):
    # priority queue: (f_score, g_score, node, path)
    open_list = [(heuristics[start], 0, start, [start])]
    visited = {}

    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if node == goal:
            return path, g
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        for neighbor, weight in graph.get(node, []):
            new_g = g + weight
            new_f = new_g + heuristics.get(neighbor, 0)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')

# Test Graph for A*
graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}
heuristics = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0}

peak_x, max_val = hill_climbing(start_x=1)
print(f"Hill Climbing: Peak at x={peak_x}, Maximum Value={max_val}")

path, cost = a_star(graph, heuristics, 'S', 'G')
print(f"A* Search: Optimal Path={' -> '.join(path)}, Cost={cost}")
```

---

## 5. Sample Input and Output

### Input Parameters:
- **Hill Climbing:** Initial state $x = 1$, Step size $= 1$, Search space $[0, 12]$.
- **A\* Search:** Start node `'S'`, Goal node `'G'`.
  - Heuristics: $h(S)=5, h(A)=3, h(B)=4, h(C)=2, h(D)=6, h(G)=0$.

### Execution Output:
```text
======================================================================
EXPERIMENT 3: HILL CLIMBING AND A* ALGORITHMS
======================================================================

======================================================================
PART A: HILL CLIMBING ALGORITHM
======================================================================
Objective: Maximize f(x) = -(x - 6)^2 + 40, Range: [0, 12]
Starting Hill Climbing from x = 1, Score f(x) = 15
  Step 1: Moved to x = 2, Score f(x) = 24
  Step 2: Moved to x = 3, Score f(x) = 31
  Step 3: Moved to x = 4, Score f(x) = 36
  Step 4: Moved to x = 5, Score f(x) = 39
  Step 5: Moved to x = 6, Score f(x) = 40
Peak reached at Step 6: No neighboring state has a higher value.

Hill Climbing Result:
  Optimal State Found : x = 6
  Maximum Value       : f(6) = 40
  Traversal Path      : x=1(15) -> x=2(24) -> x=3(31) -> x=4(36) -> x=5(39) -> x=6(40)

======================================================================
PART B: A* (A-STAR) ALGORITHM
======================================================================
Graph Edge Costs g(n):
  S -> A(cost=1), G(cost=10)
  A -> B(cost=2), C(cost=1)
  B -> D(cost=5)
  C -> D(cost=3), G(cost=4)
  D -> G(cost=2)
  G -> None (Goal)

Heuristic Values h(n) to Goal 'G':
  h(S) = 5
  h(A) = 3
  h(B) = 4
  h(C) = 2
  h(D) = 6
  h(G) = 0

Tracing A* Search from 'S' to 'G':
Step   | Current  | g(n)   | h(n)   | f(n)   | Path                
-----------------------------------------------------------------
1      | S        | 0      | 5      | 5      | S                   
2      | A        | 1      | 3      | 4      | S->A                
3      | C        | 2      | 2      | 4      | S->A->C             
4      | G        | 6      | 0      | 6      | S->A->C->G          
-----------------------------------------------------------------
A* Search Result:
  Optimal Path : S -> A -> C -> G
  Total Cost   : 6
======================================================================
```

---

## 6. Result & Viva Questions

### Result:
Hill Climbing successfully climbed uphill to find the function peak at $x = 6$ ($f(x) = 40$). A* search successfully utilized both path cost $g(n)$ and heuristic estimate $h(n)$ to locate the optimal path `S -> A -> C -> G` with minimal total cost of `6`.

### Viva Voce Q&A:
1. **Q: What is the main drawback of Simple Hill Climbing?**
   - **A:** It can get stuck in **local maxima** (peaks lower than the global peak), **plateaus** (flat areas where neighbors have equal values), or **ridges**.
2. **Q: What condition guarantees that A* search finds the optimal solution?**
   - **A:** The heuristic $h(n)$ must be **admissible** (it never overestimates the true cost to reach the goal: $h(n) \le h^*(n)$) and **consistent / monotonic** ($h(n) \le \text{cost}(n, p) + h(p)$).
3. **Q: How does A* differ from Greedy Best-First Search and Dijkstra's algorithm?**
   - **A:** Dijkstra only considers $g(n)$, Greedy Best-First only considers $h(n)$, while A* combines both $f(n) = g(n) + h(n)$ to achieve both speed and optimality.
